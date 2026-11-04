from sortedcontainers import SortedList
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        """
        We must choose k non-overlapping subarrays, each of length x.

        For each subarray, we may increase/decrease elements so that all
        x elements become equal.

        For one window, the cheapest value to make everything equal to is
        the MEDIAN.

        So:
        1. Find the cost of every possible length-x window.
        2. Use DP to choose k non-overlapping windows with minimum total cost.
        """

        n = len(nums)

        # ------------------------------------------------------------------
        # Coordinate compression
        # ------------------------------------------------------------------
        # Fenwick trees work on indexes 1..m, not arbitrary values.
        # So we map every distinct number in nums to a small rank.
        #
        # Example:
        # nums = [5, -2, 1, 3]
        # sorted unique values = [-2, 1, 3, 5]
        # rank = {-2: 1, 1: 2, 3: 3, 5: 4}
        sorted_values = sorted(set(nums))

        # rank[value] gives a 1-based index for that value.
        rank = {v: i + 1 for i, v in enumerate(sorted_values)}

        # Number of distinct values.
        m = len(sorted_values)

        # ------------------------------------------------------------------
        # Fenwick trees
        # ------------------------------------------------------------------
        # count_tree[pos] helps us find:
        #   how many current-window elements have rank <= pos.
        #
        # sum_tree[pos] helps us find:
        #   the sum of all current-window elements whose rank <= pos.
        #
        # These let us calculate the cost of making all elements equal to
        # the median in O(log m) time.
        count_tree = [0] * (m + 1)
        sum_tree = [0] * (m + 1)

        def update(pos: int, count_delta: int, sum_delta: int) -> None:
            """
            Add or remove one occurrence of a value from the Fenwick trees.

            pos         = compressed rank of the value
            count_delta = +1 when adding, -1 when removing
            sum_delta   = +value when adding, -value when removing
            """
            while pos <= m:
                count_tree[pos] += count_delta
                sum_tree[pos] += sum_delta

                # Move to the next responsible Fenwick node.
                pos += pos & -pos

        def query(pos: int):
            """
            Return:
            - count_le: number of current-window elements <= value at rank pos
            - sum_le:   sum of current-window elements <= value at rank pos
            """
            count_le = 0
            sum_le = 0

            while pos > 0:
                count_le += count_tree[pos]
                sum_le += sum_tree[pos]

                # Move to the previous responsible Fenwick node.
                pos -= pos & -pos

            return count_le, sum_le

        # ------------------------------------------------------------------
        # Current sliding window
        # ------------------------------------------------------------------
        # window keeps all x current elements in sorted order.
        # Therefore, window[x // 2] is the median.
        #
        # Example:
        # window = [-2, 1, 3]
        # x = 3
        # window[1] = 1, which is the median.
        window = SortedList()

        # Sum of all values currently inside the window.
        window_sum = 0

        def add(value: int) -> None:
            """
            Add one incoming value to the sliding window.
            """
            nonlocal window_sum

            # Insert into sorted order.
            window.add(value)

            # Update the total window sum.
            window_sum += value

            # Update Fenwick trees:
            # one more occurrence of this value exists.
            update(rank[value], 1, value)

        def remove(value: int) -> None:
            """
            Remove one outgoing value from the sliding window.
            """
            nonlocal window_sum

            # Remove exactly one occurrence from the sorted window.
            window.remove(value)

            # Update total sum.
            window_sum -= value

            # Update Fenwick trees:
            # one fewer occurrence of this value exists.
            update(rank[value], -1, -value)

        def window_cost() -> int:
            """
            Minimum operations needed to make all elements in the current
            window equal.

            The best target is the median.

            If median = m:
                cost = sum(|v - m| for every v in window)

            We split this into:
                - elements <= median: they must be increased
                - elements > median: they must be decreased
            """
            # Median of the current sorted window.
            #
            # For x = 3:
            #   window = [a, b, c]
            #   median = window[1]
            #
            # For x = 4:
            #   either middle element gives the same minimum cost,
            #   so window[2] is also valid.
            median = window[x // 2]

            # Get compressed rank of the median.
            median_rank = rank[median]

            # count_le = how many window elements are <= median
            # sum_le   = their total sum
            count_le, sum_le = query(median_rank)

            # Elements <= median must be raised to median.
            #
            # Example:
            # window = [1, 3, 7], median = 3
            # Elements <= 3: [1, 3]
            # Cost to raise them:
            #   (3 - 1) + (3 - 3) = 2
            #
            # Formula:
            #   median * count_le - sum_le
            #   = 3 * 2 - 4
            #   = 2
            left_cost = median * count_le - sum_le

            # Elements greater than median must be lowered to median.
            #
            # Example:
            # window = [1, 3, 7], median = 3
            # Elements > 3: [7]
            # Cost to lower it:
            #   7 - 3 = 4
            #
            # Formula:
            #   (window_sum - sum_le) - median * (x - count_le)
            #   = (11 - 4) - 3 * 1
            #   = 4
            right_cost = (window_sum - sum_le) - median * (x - count_le)

            # Total minimum operations for this window.
            return left_cost + right_cost

        # ------------------------------------------------------------------
        # Compute cost of every possible window
        # ------------------------------------------------------------------
        # cost[i] = minimum operations to make nums[i : i + x] uniform.
        #
        # For nums = [5, -2, 1, 3, 7, 3, 6, 4, -1], x = 3:
        #
        # cost[0] = cost of [5, -2, 1] = 7
        # cost[1] = cost of [-2, 1, 3] = 5
        # cost[2] = cost of [1, 3, 7]  = 6
        # cost[3] = cost of [3, 7, 3]  = 4
        # cost[4] = cost of [7, 3, 6]  = 4
        # cost[5] = cost of [3, 6, 4]  = 3
        # cost[6] = cost of [6, 4, -1] = 7
        cost = []

        # Build the first window: nums[0 : x].
        for i in range(x):
            add(nums[i])

        # Store cost of the first window.
        cost.append(window_cost())

        # Slide the window one index at a time.
        #
        # At each step:
        #   remove nums[i - x]  -> element leaving the window
        #   add nums[i]         -> element entering the window
        #
        # Dry run for nums = [5, -2, 1, 3, 7, 3, 6, 4, -1], x = 3:
        #
        # Initial window:
        #   [5, -2, 1]
        #   sorted: [-2, 1, 5]
        #   median = 1
        #   cost = |5-1| + |-2-1| + |1-1| = 4 + 3 + 0 = 7
        #   cost = [7]
        #
        # i = 3:
        #   remove nums[0] = 5
        #   add nums[3] = 3
        #   window = [-2, 1, 3]
        #   median = 1
        #   cost = 3 + 0 + 2 = 5
        #   cost = [7, 5]
        #
        # i = 4:
        #   remove nums[1] = -2
        #   add nums[4] = 7
        #   window = [1, 3, 7]
        #   median = 3
        #   cost = 2 + 0 + 4 = 6
        #   cost = [7, 5, 6]
        #
        # i = 5:
        #   remove nums[2] = 1
        #   add nums[5] = 3
        #   window = [3, 7, 3]
        #   sorted: [3, 3, 7]
        #   median = 3
        #   cost = 0 + 0 + 4 = 4
        #   cost = [7, 5, 6, 4]
        #
        # i = 6:
        #   remove nums[3] = 3
        #   add nums[6] = 6
        #   window = [7, 3, 6]
        #   sorted: [3, 6, 7]
        #   median = 6
        #   cost = 3 + 0 + 1 = 4
        #   cost = [7, 5, 6, 4, 4]
        #
        # i = 7:
        #   remove nums[4] = 7
        #   add nums[7] = 4
        #   window = [3, 6, 4]
        #   sorted: [3, 4, 6]
        #   median = 4
        #   cost = 1 + 2 + 0 = 3
        #   cost = [7, 5, 6, 4, 4, 3]
        #
        # i = 8:
        #   remove nums[5] = 3
        #   add nums[8] = -1
        #   window = [6, 4, -1]
        #   sorted: [-1, 4, 6]
        #   median = 4
        #   cost = 5 + 0 + 2 = 7
        #   cost = [7, 5, 6, 4, 4, 3, 7]
        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])
            cost.append(window_cost())

        # ------------------------------------------------------------------
        # DP: choose k non-overlapping windows
        # ------------------------------------------------------------------
        # dp[j][i] means:
        #   minimum total cost to choose exactly j non-overlapping windows
        #   using only the first i elements of nums.
        #
        # i represents "we have considered nums[0 : i]".
        #
        # Example:
        # dp[2][8] = best cost using 2 windows among nums[0:8].
        INF = float("inf")

        # Create a (k + 1) x (n + 1) DP table.
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        # Base case:
        # Choosing 0 windows costs 0, no matter how many elements exist.
        for i in range(n + 1):
            dp[0][i] = 0

        # Fill DP for 1 window, 2 windows, ..., k windows.
        for j in range(1, k + 1):
            for i in range(1, n + 1):

                # Option 1:
                # Do not choose a window that ends at index i - 1.
                #
                # Then the best cost is the same as using only the first
                # i - 1 elements.
                dp[j][i] = dp[j][i - 1]

                # Option 2:
                # Choose a window ending at index i - 1.
                #
                # Since every window has length x, it starts at:
                #   start = i - x
                #
                # If that start index is valid, we can choose this window.
                start = i - x

                if start >= 0:
                    # Cost if we choose this window:
                    #   best way to choose j - 1 earlier non-overlapping windows
                    #   + cost of this window starting at `start`.
                    dp[j][i] = min(
                        dp[j][i],
                        dp[j - 1][start] + cost[start]
                    )

        # Dry run of DP for:
        #   nums = [5, -2, 1, 3, 7, 3, 6, 4, -1]
        #   x = 3
        #   k = 2
        #   cost = [7, 5, 6, 4, 4, 3, 7]
        #
        # We need 2 non-overlapping windows of length 3.
        #
        # Possible good choice:
        #   window starting at 1: [-2, 1, 3], cost = 5
        #   window starting at 5: [3, 6, 4], cost = 3
        #
        # They use indices:
        #   1, 2, 3
        #   5, 6, 7
        #
        # No overlap, so total cost:
        #   5 + 3 = 8
        #
        # Therefore:
        #   dp[2][8] = 8
        #
        # The final answer is dp[k][n] = dp[2][9] = 8.
        return dp[k][n]
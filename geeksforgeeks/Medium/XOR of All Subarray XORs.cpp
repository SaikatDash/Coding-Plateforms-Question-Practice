class Solution:
    def subarrayXor(self, arr):
        # arr = input list of integers
        # n = total number of elements in the array
        n = len(arr)

        # This will store the final XOR of every subarray's XOR.
        # Start with 0 because XOR with 0 does not change a number:
        # x ^ 0 = x
        ans = 0

        # Go through every element once.
        # i is the 0-based index of arr[i].
        for i in range(n):
            # arr[i] appears in every subarray whose:
            #   - left endpoint is at index 0, 1, ..., i
            #     => (i + 1) choices
            #   - right endpoint is at index i, i+1, ..., n-1
            #     => (n - i) choices
            #
            # Therefore, arr[i] is included in:
            count = (i + 1) * (n - i)

            # XOR has this property:
            #   x ^ x = 0
            #   x ^ x ^ x = x
            #
            # So if arr[i] appears an even number of times across all
            # subarray XORs, it cancels out.
            # If it appears an odd number of times, it remains.
            if count % 2 == 1:
                # Include arr[i] in the final answer.
                ans ^= arr[i]

        # ans now equals XOR of XOR values of all possible subarrays.
        return ans
# DRY RUN for arr = [1, 2, 3]
          #
          # i = 0:
          #   arr[i] = 1
          #   count = (0 + 1) * (3 - 0) = 1 * 3 = 3
          #   3 is odd, so ans = 0 ^ 1 = 1
          #
          # i = 1:
          #   arr[i] = 2
          #   count = (1 + 1) * (3 - 1) = 2 * 2 = 4
          #   4 is even, so ans remains 1
          #
          # i = 2:
          #   arr[i] = 3
          #   count = (2 + 1) * (3 - 2) = 3 * 1 = 3
          #   3 is odd, so ans = 1 ^ 3 = 2
          #
          # Final ans = 2
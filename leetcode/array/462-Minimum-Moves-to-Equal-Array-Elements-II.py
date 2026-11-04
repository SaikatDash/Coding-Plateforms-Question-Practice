class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves
'''class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort the array so the median is easy to find.
        # After sorting, the middle element balances the smaller
        # elements on the left and larger elements on the right.
        nums.sort()

        # Find the median.
        # For an odd-length array, this is the exact middle element.
        # For an even-length array, either middle element gives the
        # same minimum total moves, so we can choose nums[n // 2].
        median = nums[len(nums) // 2]

        # This will store the total number of +/-1 operations.
        moves = 0

        # For every element, calculate how many single-unit moves
        # are needed to change it into the median.
        # Example: 1 -> 2 needs 1 move; 10 -> 2 needs 8 moves.
        for num in nums:
            # abs() is needed because an element may be either
            # smaller than the median (needs increments)
            # or larger than the median (needs decrements).
            moves += abs(num - median)

        # Return the minimum total moves.
        return moves'''

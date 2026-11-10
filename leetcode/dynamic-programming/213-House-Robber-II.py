from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        @lru_cache(None)
        def solve(index: int, start: int) -> int:
            if index < start:
                return 0
            if index == start:
                return nums[start]

            pick = nums[index] + solve(index - 2, start)
            not_pick = solve(index - 1, start)

            return max(pick, not_pick)

        # Exclude either the first or the last house
        return max(
            solve(n - 2, 0),  # houses 0 .. n-2
            solve(n - 1, 1)   # houses 1 .. n-1
        )
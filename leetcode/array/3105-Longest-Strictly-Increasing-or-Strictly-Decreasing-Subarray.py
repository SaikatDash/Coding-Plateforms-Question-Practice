from typing import List

'''class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = best = 1

        for i in range(1, len(nums)):
            inc = inc + 1 if nums[i] > nums[i - 1] else 1
            dec = dec + 1 if nums[i] < nums[i - 1] else 1
            best = max(best, inc, dec)

        return best
        '''
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = best = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            best = max(best, inc, dec)

        return best
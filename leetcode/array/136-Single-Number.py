class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans
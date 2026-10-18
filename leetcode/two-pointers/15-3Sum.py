class Solution:
    def threeSum(self, nums: List[int]) -> list[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n-2):
            # Remove duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen = set()
            for j in range(i+1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    triplet = (nums[i], complement, nums[j])
                    result.add(triplet)
                seen.add(nums[j])
        return [list(triplet) for triplet in result]
                    
                
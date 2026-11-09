class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n =len(nums)
        total_subsets = 1<<n
        result = []
        for num in range(total_subsets):
        #for num in range(1<<n):
            lst = []
            for i in range(n):
                if num &(1<<i) !=0:
                    lst.append(nums[i])
            result.append(lst)
        return result   
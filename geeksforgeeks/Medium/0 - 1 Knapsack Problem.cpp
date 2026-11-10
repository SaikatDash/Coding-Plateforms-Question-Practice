'''class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        if index == 0:
            if wt[index]<=W:
                return val[index]
            return 0
        if wt[index]>w:
            pick = float("-inf")
        else:
            pick = val[index]+self.knapsack(index-1,W-wt[index],val,wt)
        not_pick = 0+self.knapsack(index-1,W,val,wt)
        return max(pick,not_pick)
        
    def knapsack(self,W,val,wt):
        n=len(val)
        dp = [[-1 for _ in range(0,W+1)] for _ in range(n)]
        return self.knapsack(n-1,W,val,wt)
 '''          
class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        dp = [[-1] * (W + 1) for _ in range(n)]

        def knapsack(index: int, W: int, val: list[int], wt: list[int]) -> int:
            if index < 0:
                return 0

            if dp[index][W] != -1:
                return dp[index][W]

            not_pick = knapsack(index - 1, W, val, wt)

            pick = 0
            if wt[index] <= W:
                pick = val[index] + knapsack(index - 1, W - wt[index], val, wt)

            dp[index][W] = max(pick, not_pick)
            return dp[index][W]

        return knapsack(n - 1, W, val, wt)
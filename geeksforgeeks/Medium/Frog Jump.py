class Solution:
    def minCost(self, height: list[int]) -> int:
        n = len(height)
        dp = [-1] * n

        for index in range(n):
            if index == 0:
                dp[index] = 0
            elif index == 1:
                dp[index] = dp[index - 1] + abs(height[index] - height[index - 1])
            else:
                jump1 = dp[index - 1] + abs(height[index] - height[index - 1])
                jump2 = dp[index - 2] + abs(height[index] - height[index - 2])
                dp[index] = min(jump1, jump2)

        return dp[n - 1]
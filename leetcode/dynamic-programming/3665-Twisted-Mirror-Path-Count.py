class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # -1 means the move leaves the grid
        right_jump = [[-1] * n for _ in range(m)]
        down_jump = [[-1] * n for _ in range(m)]

        # Process from largest i+j to smallest
        for total in range(m + n - 2, -1, -1):
            for i in range(max(0, total - n + 1), min(m - 1, total) + 1):
                j = total - i

                # Attempt to move right
                if j + 1 >= n:
                    right_jump[i][j] = -1
                elif grid[i][j + 1] == 0:
                    right_jump[i][j] = i * n + (j + 1)
                else:
                    # Mirror: turn down and continue from (i, j+1)
                    right_jump[i][j] = down_jump[i][j + 1]

                # Attempt to move down
                if i + 1 >= m:
                    down_jump[i][j] = -1
                elif grid[i + 1][j] == 0:
                    down_jump[i][j] = (i + 1) * n + j
                else:
                    # Mirror: turn right and continue from (i+1, j)
                    down_jump[i][j] = right_jump[i + 1][j]

        dp = [0] * (m * n)
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                ways = dp[i * n + j]
                if ways == 0:
                    continue

                t = right_jump[i][j]
                if t != -1:
                    dp[t] = (dp[t] + ways) % MOD

                t = down_jump[i][j]
                if t != -1:
                    dp[t] = (dp[t] + ways) % MOD

        return dp[m * n - 1]
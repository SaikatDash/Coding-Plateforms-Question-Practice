class Solution:
    def cntSubsets(self, arr, l, r):
        MOD = 10**9 + 7
        n = len(arr)

        cnt = [0] * (n + 2)
        for x in arr:
            cnt[x] += 1

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0
        prefix_product = 1   # product of (2^cnt[i] - 1) for values < m
        used_count = 0       # number of elements with value <= m

        for m in range(r + 1):
            if m > 0:
                if cnt[m - 1] == 0:
                    break  # MEX cannot be m or greater

                prefix_product = (
                    prefix_product * (pow2[cnt[m - 1]] - 1)
                ) % MOD

            used_count += cnt[m]

            if m >= l:
                free_elements = n - used_count
                ans = (ans + prefix_product * pow2[free_elements]) % MOD

        return ans

class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # Ideal split balances both scanners:
        # a * s1 = (n - a) * s2
        # => a = n * s2 / (s1 + s2)
        ideal = (n * s2) / (s1 + s2)

        candidates = [int(ideal), int(ideal) + 1]
        ans = float('inf')

        for a in candidates:
            if 0 <= a <= n:
                time = max(a * s1, (n - a) * s2)
                ans = min(ans, time)

        return ans
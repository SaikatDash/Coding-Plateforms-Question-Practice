class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        last_seen = {}

        for i, x in enumerate(arr):
            if x in last_seen and i - last_seen[x] <= k:
                return True
            last_seen[x] = i

        return False
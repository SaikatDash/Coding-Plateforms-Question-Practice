class Solution:
    def firstElementKTime(self, arr, k):
        count = {}

        for x in arr:
            count[x] = count.get(x, 0) + 1

            if count[x] == k:
                return x

        return -1
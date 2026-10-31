class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        window = sum(arr[:totalTime])
        ans = window

        for i in range(totalTime, len(arr)):
            window += arr[i] - arr[i - totalTime]
            ans = max(ans, window)

        return ans
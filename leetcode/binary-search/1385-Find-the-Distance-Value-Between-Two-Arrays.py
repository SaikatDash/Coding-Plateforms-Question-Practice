from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Sort arr2 so we can quickly find the closest value to each arr1[i]
        arr2.sort()

        ans = 0

        for x in arr1:
            # Find the first index in sorted arr2 whose value is >= x
            i = bisect_left(arr2, x)

            # Check the closest element on the right side, if it exists
            # If |x - arr2[i]| <= d, then x is too close to arr2, so skip it
            if i < len(arr2) and arr2[i] - x <= d:
                continue

            # Check the closest element on the left side, if it exists
            # If x - arr2[i - 1] <= d, then x is too close to arr2, so skip it
            if i > 0 and x - arr2[i - 1] <= d:
                continue

            # x is farther than d from every element in arr2
            ans += 1

        return ans
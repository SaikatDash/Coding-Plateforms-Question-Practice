class Solution:
    def getMinimumDays(self, s, p):
        # Convert string to a list so we can replace characters
        arr = list(s)
        n = len(arr)

        # Step 1: Count initial bad adjacent pairs.
        # A pair (i, i+1) is bad if both characters are equal
        # and neither is '?'
        bad = 0

        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                bad += 1

        # If no bad pairs exist, no days are needed
        if bad == 0:
            return 0

        # Step 2: Replace characters day by day in the order of p[]
        for day in range(n):
            idx = p[day]

            # Check the left adjacent pair before replacement
            # If it was bad, replacing arr[idx] will fix it
            if idx > 0 and arr[idx - 1] == arr[idx]:
                bad -= 1

            # Check the right adjacent pair before replacement
            if idx + 1 < n and arr[idx] == arr[idx + 1]:
                bad -= 1

            # Replace the current character with '?'
            arr[idx] = '?'

            # If all bad pairs are fixed, return the current day
            # day is 0-based, so add 1
            if bad == 0:
                return day + 1

        # All indices are eventually replaced, so this is a safe fallback
        return n
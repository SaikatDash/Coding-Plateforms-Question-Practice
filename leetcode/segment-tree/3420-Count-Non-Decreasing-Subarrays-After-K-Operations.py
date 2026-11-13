from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()  # segments [value, count], front = leftmost
        r = n - 1
        op = 0
        ans = 0

        for l in range(n - 1, -1, -1):
            x = nums[l]
            cnt = 0

            # Prepend x: merge all segments with smaller prefix max.
            while dq and x > dq[0][0]:
                v, c = dq.popleft()
                cnt += c
                op += c * (x - v)

            dq.appendleft([x, cnt + 1])

            # Shrink from the right while cost exceeds k.
            while op > k:
                v, c = dq[-1]
                op -= v - nums[r]
                c -= 1
                if c == 0:
                    dq.pop()
                else:
                    dq[-1][1] = c
                r -= 1

            ans += r - l + 1

        return ans
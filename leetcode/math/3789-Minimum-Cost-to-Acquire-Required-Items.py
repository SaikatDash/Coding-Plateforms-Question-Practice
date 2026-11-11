class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        pair = min(need1, need2)
        ans = pair * min(costBoth, cost1 + cost2)

        rem1 = need1 - pair
        rem2 = need2 - pair

        ans += rem1 * min(cost1, costBoth)
        ans += rem2 * min(cost2, costBoth)

        return ans
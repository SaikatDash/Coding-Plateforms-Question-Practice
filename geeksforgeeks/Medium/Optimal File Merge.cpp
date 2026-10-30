import heapq

class Solution:
    def minComputation(self, files):
        if len(files) <= 1:
            return 0

        heapq.heapify(files)
        total = 0

        while len(files) > 1:
            x = heapq.heappop(files)
            y = heapq.heappop(files)
            cost = x + y
            total += cost
            heapq.heappush(files, cost)

        return total
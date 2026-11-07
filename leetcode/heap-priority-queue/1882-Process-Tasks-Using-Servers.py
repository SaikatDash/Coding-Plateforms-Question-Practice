import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)

        busy = []  # (free_time, weight, server_index)
        ans = []

        for j, duration in enumerate(tasks):
            # Release servers whose work ends by time j
            while busy and busy[0][0] <= j:
                _, weight, i = heapq.heappop(busy)
                heapq.heappush(free, (weight, i))

            if free:
                weight, i = heapq.heappop(free)
                time = j
            else:
                # Wait for the earliest available server.
                # Heap order (free_time, weight, index) guarantees
                # this is the correct server to use.
                time, weight, i = heapq.heappop(busy)

            ans.append(i)
            heapq.heappush(busy, (time + duration, weight, i))

        return ans
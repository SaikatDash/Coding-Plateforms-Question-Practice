from typing import List
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][run]: minimum cost to reach node with trailing run length run
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]  # cost, node, current run length

        while heap:
            cost, u, run = heapq.heappop(heap)
            if cost > dist[u][run]:
                continue
            if u == n - 1:
                return cost

            for v, w in graph[u]:
                new_run = run + 1 if labels[u] == labels[v] else 1
                if new_run > k:
                    continue

                new_cost = cost + w
                if new_cost < dist[v][new_run]:
                    dist[v][new_run] = new_cost
                    heapq.heappush(heap, (new_cost, v, new_run))

        return -1
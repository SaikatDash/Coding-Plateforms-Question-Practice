import heapq

class Solution:
    def shortestPath(self, V, edges, src, dest):

        adj = [[] for _ in range(V + 1)]

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        # Dijkstra from destination
        dist = [float('inf')] * (V + 1)
        dist[dest] = 0

        pq = [(0, dest)]

        while pq:
            d, u = heapq.heappop(pq)

            if d != dist[u]:
                continue

            for v, wt in adj[u]:
                new_dist = d + wt

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        if dist[src] == float('inf'):
            return [-1]

        # Reconstruct lexicographically smallest shortest path
        path = [src]
        current = src

        while current != dest:

            candidates = []

            for v, wt in adj[current]:
                if wt + dist[v] == dist[current]:
                    candidates.append(v)

            if not candidates:
                return [-1]

            current = min(candidates)
            path.append(current)

        return path
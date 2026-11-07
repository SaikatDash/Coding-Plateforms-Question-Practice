class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist = [-1]*V
        queue = deque()
        queue.append([src,0])# this zero is an dist_travl initial value
        dist[src] = 0
        while len(queue)!=0:
            node,dist_travl = queue.popleft()
            dist.append(dist_travl)
            for node in adj[node]:
                if dist[node] == -1:
                    dist[node] = dist_travl + 1
                    queue.append([node,dist_travl+1])
        return dist[dest]
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        self.time = 0

        def dfs(node):
            visited[node] = True
            found = hasApple[node]

            for child in adj[node]:
                if not visited[child] and dfs(child):
                    self.time += 2
                    found = True

            return found

        dfs(0)
        return self.time
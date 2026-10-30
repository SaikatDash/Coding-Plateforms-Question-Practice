class Solution:
    def dfs(self, adj):
        visited = [False] * len(adj)
        ans = []

        def dfs_util(node):
            visited[node] = True
            ans.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(0)
        return ans
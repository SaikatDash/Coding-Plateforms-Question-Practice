class Solution:
    def dfs(self, adj):
        visited = [False] * len(adj)
        ans = []

        def dfs_util(node):
            visited[node] = 1
            ans.append(node)

            for n in adj[node]:
                if not visited[n]:
                    dfs_util(n)

        dfs_util(0)
        return ans
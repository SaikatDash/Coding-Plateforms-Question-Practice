<<<<<<< HEAD:geeksforgeeks/Easy/DFS of Graph.py
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
=======
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
>>>>>>> 954884ba9f197bce6b7aa147956845d0a7ea2dd8:geeksforgeeks/Easy/DFS of Graph.js
        return ans
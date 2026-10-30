class Solution:
    def checkEdge(self, adj, u, v):
        return v in adj[u]
class Solution:
    def dfs(self, node, stack, visited, adj_list):
        visited[node] = 1

        for adjnode, d in adj_list[node]:
            if visited[adjnode] == 0:
                self.dfs(adjnode, stack, visited, adj_list)

        stack.append(node)

    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj_list = [[] for _ in range(V)]

        for u, v, d in edges:
            adj_list[u].append([v, d])

        visited = [0] * V
        stack = []

        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, stack, visited, adj_list)

        distance = [float("inf")] * V
        distance[0] = 0

        while len(stack) != 0:
            node = stack.pop()
            dist = distance[node]

            for adjNode, d in adj_list[node]:
                new_dist = dist + d

                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist

        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance
'''
class Solution:
    def dfs(self, node, stack, visited, adj_list):
        # Mark current node as visited
        visited[node] = 1

        # Visit all adjacent nodes first
        for adjnode in adj_list[node]:
            if visited[adjnode] == 0:
                self.dfs(adjnode, stack, visited, adj_list)

        # After visiting all children, push node into stack
        # This creates reverse topological order
        stack.append(node)

    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        # Build adjacency list
        # adj_list[u] = [[v, weight], [v2, weight2], ...]
        adj_list = [[] for _ in range(V)]

        for u, v, d in edges:
            adj_list[u].append([v, d])

        # Visited array for DFS
        visited = [0] * V

        # Stack for topological sort
        stack = []

        # Start DFS from every unvisited node
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, stack, visited, adj_list)

        # Initialize all distances to infinity
        # distance[i] means shortest distance from node 0 to node i
        distance = [float("inf")] * V

        # Distance from source node 0 to itself is 0
        distance[0] = 0

        # Process nodes in topological order
        # stack was filled in reverse topological order,
        # so pop() gives correct topological order
        while len(stack) != 0:
            node = stack.pop()

            # dist = current shortest distance from 0 to node
            dist = distance[node]

            # Relax every outgoing edge from node
            for adjNode, d in adj_list[node]:
                # Distance to adjNode if we go through current node
                new_dist = dist + d

                # If this path is shorter, update distance
                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist

        # If a node is still infinity, it is unreachable from 0
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance
        '''
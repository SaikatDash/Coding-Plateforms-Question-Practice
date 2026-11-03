class Solution:
    def topoSort(self, adj: list[list[int]]) -> list[int]:
        # adj = [[1, 2], [3], [3], []]
        #
        # Graph:
        # 0 -> 1
        # 0 -> 2
        # 1 -> 3
        # 2 -> 3
        #
        # Dry run:
        # Start from 0
        # dfs(0)
        #   visit 0
        #   go to 1
        #     dfs(1)
        #       visit 1
        #       go to 3
        #         dfs(3)
        #           visit 3
        #           no neighbors
        #           push 3
        #           stack = [3]
        #       push 1
        #       stack = [3, 1]
        #   go to 2
        #     dfs(2)
        #       visit 2
        #       go to 3
        #       3 already visited
        #       push 2
        #       stack = [3, 1, 2]
        #   push 0
        #   stack = [3, 1, 2, 0]
        #
        # Reverse stack:
        # [0, 2, 1, 3]

        V = len(adj)  # V = 4

        visited = [False] * V
        # visited = [False, False, False, False]

        stack = []
        # stack = []

        def dfs(node):
            # node is the current vertex

            visited[node] = True
            # Example: dfs(0) -> visited = [True, False, False, False]

            for i in adj[node]:
                # Visit all neighbors of current node

                if not visited[i]:
                    dfs(i)
                    # Explore neighbor before current node

            stack.append(node)
            # Push current node after all its neighbors are done

        for i in range(V):
            # Check every vertex

            if not visited[i]:
                dfs(i)
                # Start DFS if not visited

        return stack[::-1]
        # Reverse DFS finish order to get topological sort
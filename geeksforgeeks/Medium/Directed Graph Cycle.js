from collections import deque

class Solution:
    def isCyclic(self, adj):
        V = len(adj)
        indegrees = [0] * V

        for u in range(V):
            for v in adj[u]:
                indegrees[v] += 1

        queue = deque()
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        processed = 0

        while queue:
            current_node = queue.popleft()
            processed += 1

            for adjNode in adj[current_node]:
                indegrees[adjNode] -= 1

                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        return processed != V
        
'''from collections import deque  # Provides a queue with efficient removal from the front.


class Solution:
    def isCyclic(self, adj):
        # Dry-run example:
        # adj = [[1], [2], [1]]
        # Edges: 0 -> 1, 1 -> 2, 2 -> 1
        # Vertices 1 and 2 form a directed cycle.

        # Count the vertices.
        # Dry run: V = 3.
        V = len(adj)

        # indegrees[v] counts the incoming edges to vertex v.
        # Dry run: initially indegrees = [0, 0, 0].
        indegrees = [0] * V

        # Visit every edge u -> v and increase v's indegree.
        for u in range(V):
            for v in adj[u]:
                indegrees[v] += 1
                # Dry run:
                # 0 -> 1: indegrees = [0, 1, 0]
                # 1 -> 2: indegrees = [0, 1, 1]
                # 2 -> 1: indegrees = [0, 2, 1]

        # Collect vertices with no incoming edges.
        # These vertices can be processed immediately.
        queue = deque()
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        # Dry run: only vertex 0 has indegree zero.
        # queue = deque([0])

        # Track how many vertices we successfully process.
        processed = 0

        # Continue until there are no available vertices.
        while queue:
            # Remove the next vertex from the front.
            # Dry run: current_node = 0; queue becomes empty.
            current_node = queue.popleft()

            # Count this vertex as processed.
            # Dry run: processed = 1.
            processed += 1

            # Remove the current vertex's outgoing edges logically
            # by decreasing the indegree of each neighbor.
            for adjNode in adj[current_node]:
                indegrees[adjNode] -= 1
                # Dry run: neighbor 1's indegree decreases from 2 to 1.
                # indegrees = [0, 1, 1]

                # A neighbor becomes available only when all its
                # incoming edges have been removed.
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

                # Dry run: vertex 1 still has indegree 1,
                # so it is not added to the queue.

        # Dry run: the queue is empty, so processing stops.
        # Vertices 1 and 2 remain blocked by their cycle.
        # processed = 1, V = 3 -> return True.
        #
        # If every vertex is processed, there is no cycle:
        # processed == V -> return False.
        return processed != V
        '''
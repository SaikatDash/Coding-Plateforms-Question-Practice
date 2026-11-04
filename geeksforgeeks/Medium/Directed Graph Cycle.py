from collections import deque

class Solution:
    def isCyclic(self, adj):
        V = len(adj)
        indegrees = [0] * V

        for u in range(V):
            for v in adj[u]:
                indegrees[v] += 1

        queue = deque()
        result = []

        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for adjNode in adj[current_node]:
                indegrees[adjNode] -= 1

                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        return len(result) != V
        
'''from collections import deque  # Queue for vertices with indegree zero.


   class Solution:
       def isCyclic(self, adj):
           # Dry run: adj = [[1], [2], [1]]
           # Edges: 0 -> 1, 1 -> 2, 2 -> 1.
           # Vertices 1 and 2 form a cycle.

           # Find the number of vertices.
           # Dry run: V = 3.
           V = len(adj)

           # Store the number of incoming edges for each vertex.
           # Dry run: indegrees = [0, 0, 0].
           indegrees = [0] * V

           # For every edge u -> v, increase v's indegree.
           for u in range(V):
               for v in adj[u]:
                   indegrees[v] += 1

           # Dry run:
           # After 0 -> 1: [0, 1, 0]
           # After 1 -> 2: [0, 1, 1]
           # After 2 -> 1: [0, 2, 1]

           queue = deque()

           # Store vertices in the order they are removed from the queue.
           result = []

           # Add all vertices with no incoming edges.
           for i in range(V):
               if indegrees[i] == 0:
                   queue.append(i)

           # Dry run: queue = deque([0]), result = [].

           while queue:
               # Remove the front vertex.
               # Dry run: current_node = 0, queue = deque([]).
               current_node = queue.popleft()

               # Save the removed vertex in the result array.
               # Dry run: result = [0].
               result.append(current_node)

               # Decrease each neighbor's indegree to represent
               # removing the outgoing edges of current_node.
               for adjNode in adj[current_node]:
                   indegrees[adjNode] -= 1

                   # Dry run: edge 0 -> 1 is removed.
                   # indegrees changes from [0, 2, 1] to [0, 1, 1].

                   # Add a neighbor when no incoming edges remain.
                   if indegrees[adjNode] == 0:
                       queue.append(adjNode)

                   # Dry run: vertex 1 still has indegree 1,
                   # so it is not added to the queue.

           # Dry run: the queue is empty and result = [0].
           # Vertices 1 and 2 could not be added because of the cycle.
           # len(result) = 1, V = 3 -> return True.
           #
           # If result contains all V vertices, there is no cycle.
           return len(result) != V
        '''
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for u, v in prerequisites:
            # v is prerequisite for u
            adj_list[v].append(u)
            indegrees[u] += 1

        queue = deque()
        result = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for adjNode in adj_list[current_node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        return len(result) == numCourses
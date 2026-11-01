from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = [[False] * cols for _ in range(rows)]
        distance = [[0] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, d = queue.popleft()
            distance[r][c] = d

            for dr, dc in directions:
                new_i, new_j = r + dr, c + dc

                if (
                    0 <= new_i < rows
                    and 0 <= new_j < cols
                    and not visited[new_i][new_j]
                ):
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j, d + 1))

        return distance
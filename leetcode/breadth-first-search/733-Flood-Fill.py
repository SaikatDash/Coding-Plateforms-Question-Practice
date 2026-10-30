from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        initial_color = image[sr][sc]

        if initial_color == color:
            return image

        visited = [row[:] for row in image]
        queue = deque([(sr, sc)])
        visited[sr][sc] = color

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            i, j = queue.popleft()

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if visited[new_i][new_j] != initial_color:
                    continue

                visited[new_i][new_j] = color
                queue.append((new_i, new_j))

        return visited
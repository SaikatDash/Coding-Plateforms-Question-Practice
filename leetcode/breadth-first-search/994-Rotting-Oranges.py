#from collection import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)

        fresh_count = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid_copy[i][j] == 2:
                    queue.append((i, j))
                elif grid_copy[i][j] == 1:
                    fresh_count += 1

        minutes = 0
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue and fresh_count > 0:
            minutes += 1

            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dx, dy in directions:
                    new_i = i + dx
                    new_j = j + dy

                    if not (0 <= new_i < rows and 0 <= new_j < cols):
                        continue

                    if grid_copy[new_i][new_j] != 1:
                        continue

                    grid_copy[new_i][new_j] = 2
                    fresh_count -= 1
                    queue.append((new_i, new_j))

        return minutes if fresh_count == 0 else -1

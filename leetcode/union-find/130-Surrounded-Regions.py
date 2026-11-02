class Solution:
    def dfs(self, r, c, visited, rows, cols, board):
        # Base case 1:
        # If the current cell (r, c) is outside the board,
        # stop the recursion immediately.
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        # Base case 2:
        # If the current cell is NOT 'O', there is nothing to mark.
        # We only care about 'O' cells.
        if board[r][c] != "O":
            return

        # Base case 3:
        # If this 'O' cell has already been visited,
        # do not process it again. This prevents infinite recursion.
        if visited[r][c] == 1:
            return

        # Mark the current 'O' cell as visited.
        # This means it is connected to a boundary 'O',
        # so it should NOT be flipped to 'X' later.
        visited[r][c] = 1

        # Move upward: check the cell above the current cell.
        self.dfs(r - 1, c, visited, rows, cols, board)

        # Move left: check the cell to the left of the current cell.
        self.dfs(r, c - 1, visited, rows, cols, board)

        # Move right: check the cell to the right of the current cell.
        self.dfs(r, c + 1, visited, rows, cols, board)

        # Move downward: check the cell below the current cell.
        self.dfs(r + 1, c, visited, rows, cols, board)

    def solve(self, board: list[list[str]]) -> None:
        # rows = total number of rows in the board
        rows = len(board)

        # cols = total number of columns in the board
        cols = len(board[0])

        # Create a visited matrix of the same size as the board.
        # Initially, every value is 0, meaning no cell has been visited yet.
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # Step 1:
        # Traverse every cell on the boundary of the board.
        # Boundary cells are the first row, last row,
        # first column, and last column.
        for r in range(rows):
            for c in range(cols):

                # Check whether the current cell lies on the boundary.
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:

                    # If the boundary cell is 'O' and has not been visited,
                    # start DFS from it.
                    if board[r][c] == "O" and visited[r][c] == 0:
                        self.dfs(r, c, visited, rows, cols, board)

        # Step 2:
        # After DFS, every 'O' connected to the boundary is marked as visited.
        # Any remaining unvisited 'O' is completely surrounded,
        # so it must be flipped to 'X'.
        for r in range(rows):
            for c in range(cols):

                # If the cell is still 'O' and was never visited by DFS,
                # then it is surrounded.
                if board[r][c] == "O" and visited[r][c] == 0:

                    # Flip the surrounded 'O' to 'X'.
                    board[r][c] = "X"
    
    # Input board:
# [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"]
# ]

# Initial visited matrix:
# [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

# Step 1: Check boundary cells.
# Boundary 'O' cells:
# - board[3][1] = "O"

# Start DFS from (3, 1).
# Mark visited[3][1] = 1.

# DFS checks:
# Up: (2, 1) = "X" -> stop
# Left: (3, 0) = "X" -> stop
# Right: (3, 2) = "X" -> stop
# Down: (4, 1) -> outside board -> stop

# So only the boundary 'O' at (3, 1) is marked safe.

# Visited matrix after DFS:
# [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 1, 0, 0]
# ]

# Step 2: Flip unvisited 'O' cells to 'X'.
# Unvisited 'O' cells:
# - (1, 1)
# - (1, 2)
# - (2, 2)

# These are surrounded, so they become 'X'.

# Final board:
# [
#     ["X", "X", "X", "X"],
#     ["X", "X", "X", "X"],
#     ["X", "X", "X", "X"],
#     ["X", "O", "X", "X"]
# ]
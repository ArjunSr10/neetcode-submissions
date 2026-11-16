
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(row, col):
            if (row < 0 or row >= m or
                col < 0 or col >= n or
                board[row][col] != "O"):
                return

            board[row][col] = "T"

            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)

        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = set()

        def backtrack(row, col, i):
            if i == len(word):
                return True

            if (row < 0 or row >= n or
                col < 0 or col >= m or
                (row, col) in visited or
                board[row][col] != word[i]):
                return False

            visited.add((row, col))

            result = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row - 1, col, i + 1) or
                backtrack(row, col + 1, i + 1) or
                backtrack(row, col - 1, i + 1)
            )

            visited.remove((row, col))

            return result

        for row in range(n):
            for col in range(m):
                if backtrack(row, col, 0):
                    return True

        return False
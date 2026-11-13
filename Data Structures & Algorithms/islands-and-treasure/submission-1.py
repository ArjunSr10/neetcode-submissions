
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2 ** 31) - 1
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        q = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()

            for rowChange, colChange in directions:
                r = row + rowChange
                c = col + colChange
                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == INF:
                        grid[r][c] = grid[row][col] + 1
                        q.append((r, c))
            
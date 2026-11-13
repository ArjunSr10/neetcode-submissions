class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        mins = 0
        fresh = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for rowChange, colChange in directions:
                    r = row + rowChange
                    c = col + colChange

                    if 0 <= r < m and 0 <= c < n:
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                            fresh -= 1
                            q.append((r, c))

            mins += 1

        return mins if fresh == 0 else -1

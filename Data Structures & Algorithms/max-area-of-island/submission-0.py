class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0

        def dfs(row, col):
            if grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))
            curArea = 1
            for direction in directions:
                rowChange = row + direction[0]
                colChange = col + direction[1]
                if 0 <= rowChange < n and 0 <= colChange < m:
                    curArea += dfs(rowChange, colChange)

            return curArea

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and (row, col) not in visited:
                    islandArea = dfs(row, col)
                    maxArea = max(maxArea, islandArea)

        return maxArea
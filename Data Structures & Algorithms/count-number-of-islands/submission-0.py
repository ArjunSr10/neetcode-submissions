class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        count = 0

        def dfs(row, col):
            if grid[row][col] == "0" or (row, col) in visited:
                return
            
            visited.add((row, col))
            for direction in directions:
                rowChange = row + direction[0]
                colChange = col + direction[1]
                if rowChange < n and rowChange >= 0 and colChange < m and colChange >= 0:
                    dfs(rowChange, colChange)
                    
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    count += 1

        return count


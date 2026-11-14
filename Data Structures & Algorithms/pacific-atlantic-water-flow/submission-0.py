class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        result = []
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited):
            if (row, col) in visited:
                return

            visited.add((row, col))

            for dr, dc in directions:
                rowChange = row + dr
                colChange = col + dc
                if (0 <= rowChange < m and 0 <= colChange < n 
                and heights[rowChange][colChange] >= heights[row][col]):
                    dfs(rowChange, colChange, visited)

        for col in range(n):
            dfs(0, col, pacific)
            dfs(m - 1, col, atlantic)

        for row in range(m):
            dfs(row, 0, pacific)
            dfs(row, n - 1, atlantic)

        for row in range(m):
            for col in range(n):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result
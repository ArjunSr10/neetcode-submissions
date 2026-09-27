class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1
        
        while top <= bot:
            targetRow = (top + bot) // 2
            if matrix[targetRow][0] > target:
                bot = targetRow - 1
            elif matrix[targetRow][n - 1] < target:
                top = targetRow + 1
            else:
                break

        l, r = 0, n - 1

        while l <= r:
            median = (l + r) // 2
            if matrix[targetRow][median] > target:
                r = median - 1
            elif matrix[targetRow][median] < target:
                l = median + 1
            else:
                return True
        
        return False
        


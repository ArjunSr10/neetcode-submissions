class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtracking(openNumber, closeNumber):
            if openNumber == closeNumber == n:
                res.append("".join(stack))
                return
            
            if openNumber < n:
                stack.append("(")
                backtracking(openNumber + 1, closeNumber)
                stack.pop()

            if closeNumber < openNumber:
                stack.append(")")
                backtracking(openNumber, closeNumber + 1)
                stack.pop()

        backtracking(0, 0)
        return res
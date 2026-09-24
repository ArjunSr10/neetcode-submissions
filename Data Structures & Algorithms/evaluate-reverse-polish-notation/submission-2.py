class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 + op2)
            elif token == "-":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 - op2)
            elif token == "*":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 * op2)
            elif token == "/":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(int(op1 / op2))
            else:
                stack.append(token)
            
        return int(stack[-1])


                
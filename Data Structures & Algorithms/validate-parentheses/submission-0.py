class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            if not stack:
                return False
            elif char ==  ')':
                if stack.pop() != '(':
                    return False
            elif char ==  ']':
                if stack.pop() != '[':
                    return False
            elif char ==  '}':
                if stack.pop() != '{':
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def backtrack(i, j):
            if j == len(s):
                res.append(sub.copy())
                return
            
            if i >= len(s):
                return
            
            if self.isPalindrome(s[j:i+1]):
                sub.append(s[j:i+1])
                backtrack(i + 1, i + 1)
                sub.pop()
            
            backtrack(i + 1, j)
        
        backtrack(0, 0)
        return res

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

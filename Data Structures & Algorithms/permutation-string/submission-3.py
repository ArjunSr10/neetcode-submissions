class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Arr = [0] * 26
        for c in s1:
            s1Arr[ord(c) - ord('a')] += 1

        l, r = 0, len(s1)
        s2Arr = [0] * 26
        
        for c in s2[l:r]:
            s2Arr[ord(c) - ord('a')] += 1

        while r <= len(s2):
            if s1Arr == s2Arr:
                return True 

            if r == len(s2):
                break 
                
            s2Arr[ord(s2[l]) - ord('a')] -= 1
            s2Arr[ord(s2[r]) - ord('a')] += 1

            l += 1
            r += 1
        
        return False

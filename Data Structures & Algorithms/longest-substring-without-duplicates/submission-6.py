class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 1
        charSet = set()
        charSet.add(s[l])
        maxLength = 1

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxLength = max(maxLength, r - l + 1)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1

        return maxLength
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        length = 1
        res = 0

        for elem in nums:
            if (elem - 1) not in hashSet:
                flag = True
                while flag == True:
                    if (elem + 1) in hashSet:
                        elem += 1
                        length += 1
                    else:
                        res = max(res, length)
                        length = 1
                        flag = False
        
        return res
            
        
        
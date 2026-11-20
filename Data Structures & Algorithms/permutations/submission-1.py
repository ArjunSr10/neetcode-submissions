class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            
            for n in nums:
                if n not in sub:
                    sub.append(n)
                    backtrack(sub)
                    sub.remove(n)
        
        backtrack([])
        return res
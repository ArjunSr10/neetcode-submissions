class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
            
            elif sum > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, sum + nums[i])
            subset.pop()
            dfs(i + 1, sum)
        
        dfs(0, 0)
        return res

            
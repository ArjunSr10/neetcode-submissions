class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(indices):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for j in range(len(nums)):
                if j not in indices:
                    subset.append(nums[j])
                    indices.add(j)

                    dfs(indices)

                    indices.remove(j)
                    subset.pop()

        indices = set()
        dfs(indices)
        return res
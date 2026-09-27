class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        
        while l <= r:
            median = (r + l) // 2
            if nums[median] < target:
                l = median + 1
            elif nums[median] > target:
                r = median - 1
            else:
                return median
        
        return -1
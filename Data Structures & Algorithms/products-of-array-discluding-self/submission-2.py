class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftPrefix = [1] * n
        rightPrefix = [1] * n
        res = [0] * n
        leftProduct = 1
        rightProduct = 1
        
        for i in range(n):
            leftPrefix[i] = leftProduct
            leftProduct *= nums[i]
        
        for i in range(n - 1, -1, -1):
            rightPrefix[i] = rightProduct
            rightProduct *= nums[i]

        for i in range(n):
            res[i] = leftPrefix[i] * rightPrefix[i]

        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        longest = 1

        for num in numSet:
            if (num - 1) not in numSet:
                tmp = 1
                while (num + tmp) in numSet:
                    tmp += 1
                longest = max(longest, tmp)

        return longest

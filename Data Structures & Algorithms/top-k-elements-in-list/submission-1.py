class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
        
        sortedList = sorted(hashTable, key=hashTable.get, reverse=True)
        return sortedList[0:k]
        
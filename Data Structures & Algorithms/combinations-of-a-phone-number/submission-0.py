class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phonebook = {"2": "abc", 
                "3": "def", 
                "4": "ghi", 
                "5": "jkl", 
                "6": "mno", 
                "7": "pqrs", 
                "8": "tuv", 
                "9": "wxyz"}

        res = []
        substring = ""

        def backtrack(i):
            nonlocal substring

            if i >= len(digits):
                res.append(substring)
                return

            for letter in phonebook.get(digits[i]):
                substring += letter
                backtrack(i + 1)
                substring = substring[:-1]

        backtrack(0)
        return res
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(rem,curr):
            print(rem,curr)
            if len(curr)==len(digits):
                res.append(curr)
                return
            
            for ch in digitToChar[rem[0]]:
                dfs(rem[1:],curr+ch)

        
        dfs(digits,"")
        return res
        
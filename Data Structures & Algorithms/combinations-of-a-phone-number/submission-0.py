class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
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
        res=[""]

        def backtrack(i):
            nonlocal res
            if i>=len(digits):
                return
            alphabets=digitToChar[digits[i]]

            new_res=[]
            for alphabet in alphabets:
                for r in res:
                    new_res.append(r+alphabet)
            res=new_res.copy()
            backtrack(i+1)

        backtrack(0)
        return res



        
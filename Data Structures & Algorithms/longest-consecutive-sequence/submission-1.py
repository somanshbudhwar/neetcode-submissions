class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res={}
        for n in nums:
            if n not in res:
                res[n]=None
        print(res)

        for n in nums:
            if n+1 in res:
                res[n]=n+1
        print(res)

        max_len=0
        for r in res:
            p=r
            length=1
            while res[p] is not None:
                length+=1
                p=res[p]

            if length>max_len:
                max_len=length
        return max_len
        
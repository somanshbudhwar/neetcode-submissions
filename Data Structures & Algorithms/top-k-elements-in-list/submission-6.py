class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        base=[0 for i in range(2001)]

        for n in nums:
            base[n+1000]+=1
        
        res=[]
        for i in range(k):
            r = base.index(max(base))
            # print(r, max(base))
            base[r]=0
            res.append(r-1000)


        return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}

        for n in nums:
            if n in hash_set:
                hash_set[n]+=1
            else:
                hash_set[n]=1
        res = []

        for i in hash_set:
            res.append([i,hash_set[i]])
        
        res.sort(key=lambda x: x[1], reverse=True)
        final = [i[0] for i in res[:k]]
        return final

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        tuple_count = list(counts.items())
        tuple_count.sort(key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(tuple_count[i][0])
        return res
        
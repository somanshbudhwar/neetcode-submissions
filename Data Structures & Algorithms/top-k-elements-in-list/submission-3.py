from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        max_count = max(counts.values())
        freq_dict = defaultdict(list)

        for num, count in counts.items():
            freq_dict[count].append(num)

        res = []
        for i in range(max_count,0,-1):
            res+=freq_dict[i][:k]
            if len(res)>=k:
                break

        return res
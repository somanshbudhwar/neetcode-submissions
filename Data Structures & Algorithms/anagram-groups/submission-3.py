class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trace = defaultdict(list)

        for s in strs:
            t=[0]*26
            for i in s:
                t[ord(i)-97]+=1
            key=tuple(t)
            trace[key].append(s)
            
        return list(trace.values())

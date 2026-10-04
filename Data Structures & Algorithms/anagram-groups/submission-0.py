class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for i in strs:
            key = "".join(sorted([s for s in i]))
            if key in res:
                res[key].append(i)
            else:
                res[key]=[i]
        return list(res.values())
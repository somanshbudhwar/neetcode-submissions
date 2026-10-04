class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            # CRITICAL PART
            count = [0] * 26
            for alphabet in word:
                count[ord(alphabet)-ord('a')]+=1
            res[tuple(count)].append(word)
        return list(res.values())
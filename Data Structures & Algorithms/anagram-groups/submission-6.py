class Solution:
    def create_tuple(self, text):
        res = [0 for i in range(97,123)]
        for t in text:
            res[ord(t)-97]+=1
        return tuple(res)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}

        for word in strs:
            word_tuple = self.create_tuple(word)
            if word_tuple not in groups:
                groups[word_tuple]=[word]
            else:
                groups[word_tuple]+=[word]
        return list(groups.values())
        
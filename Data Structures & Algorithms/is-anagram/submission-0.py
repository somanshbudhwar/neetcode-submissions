class Solution:
    def create_dict_count(self, text):
        res={}
        for t in text:
            if t not in res:
                res[t]=1
            else:
                res[t]+=1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return self.create_dict_count(s)==self.create_dict_count(t)


        
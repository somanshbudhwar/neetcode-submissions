class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        l=0
        base_dict = {}
        for c in s1:
            if c not in base_dict:
                base_dict[c]=1
            else:
                base_dict[c]+=1
        
        while (l+window_len-1)<len(s2):
            comp_dict = {}
            for c in s2[l:l+window_len]:
                if c not in comp_dict:
                    comp_dict[c]=1
                else:
                    comp_dict[c]+=1
            # print(s2[l:l+window_len],comp_dict)
            if base_dict==comp_dict:
                return True
            l+=1
        return False


        
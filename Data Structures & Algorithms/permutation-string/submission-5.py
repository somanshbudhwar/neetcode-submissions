class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)

        base_dict=defaultdict(int)
        for i in s1:
            base_dict[i]+=1
        
        comp_dict=defaultdict(int)
        for i in s2[:window_len]:
            comp_dict[i]+=1

        
        l=0

        while (l+window_len-1)<=len(s2):
            print(base_dict)
            print(comp_dict)
            print('*'*100)
            if base_dict==comp_dict:
                return True
            
            comp_dict[s2[l]]-=1
            if not comp_dict[s2[l]]:
                comp_dict.pop(s2[l])
            l+=1
            # CRITICAL IDEA
            if l+window_len-1>=len(s2):
                break
            comp_dict[s2[l+window_len-1]]+=1
            

        return False

        


        
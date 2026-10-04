class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        r=0
        max_len=0
        curr_len=0
        curr_set=set()

        while r<len(s):
            while s[r] not in curr_set:
                curr_set.add(s[r])
                curr_len+=1
                r+=1
                print(curr_set, l, r)
                if r==len(s):
                    if curr_len>max_len:
                        max_len=curr_len
                    return max_len
                
            if curr_len>max_len:
                max_len=curr_len

            while s[r] in curr_set:
                curr_set.remove(s[l])
                curr_len-=1
                l+=1
        return max_len
        
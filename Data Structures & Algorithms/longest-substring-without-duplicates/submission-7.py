class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        r=0
        max_len=0
        curr_set=set()
        count=0

        while l<len(s) and r<len(s):
            if s[r] not in curr_set:
                curr_set.add(s[r])
                max_len=max(len(curr_set),max_len)
                r+=1
            else:
                curr_set.discard(s[l])
                l += 1
            
        return max_len
            


        
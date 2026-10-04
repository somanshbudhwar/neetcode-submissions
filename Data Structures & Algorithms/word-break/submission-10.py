# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # def dfs(index,data):
        #     # print(index,"::",data)
        #     if index<10:
        #         return False
        #     if index==0:
        #         return True
        #     if index<0:
        #         return False
            
        #     for word in wordDict:
        #         print("Comparing: ",word,"---",data[index:index+len(word)])
        #         if word==data[index-len(word):index]:
        #             next_pattern = dfs(index-len(word),s)
        #             if next_pattern:
        #                 # print("Pattern match")
        #                 return True
        #     return False
        # wordDict.sort(key=lambda x:len(x), reverse=True)

        # return dfs(len(s),s)
        # l=0
        # r=0
        # memo={}

        # while r<len(s)+1:
        #     if s[l:r] in memo:
        #         memo[s[0:r]]=True
        #         l=r
        #     if s[l:r] in wordDict:
        #         memo[s[0:r]]=True
        #         l=r
        #     r+=1
        # print(memo)
        # return memo.get(s,False)     
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            print(dp)
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]      








                        

        
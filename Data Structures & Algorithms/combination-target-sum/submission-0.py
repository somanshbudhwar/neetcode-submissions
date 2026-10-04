class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=list()
        nums.sort()
        mp = {}

        def explore(t,subset):
            if (t,tuple(sorted(subset))) in mp:
                return None
            for num in nums:
                subset.append(num)
                if t-num<0:
                    subset.pop()
                    break
                elif t-num==0:
                    mp[(t,tuple(sorted(subset)))]=True
                    res.append(subset.copy())
                    # print(t,num,subset)
                    subset.pop()
                else:
                    explore(t-num,subset)
                    subset.pop()
        
        explore(target,[])
        result=[]
        for key in mp:
            if list(key[1]) not in result:
                result.append(list(key[1]))
        
        return result
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def combinatorics(n,c):
            if c==1:
                res = [[i] for i in range(n)]
                return res
            else:
                combos = combinatorics(n,c-1)
                # print(n,c,combinatorics(n,c-1))
                for e in combinatorics(n,c-1):
                    if len(e)==c-1:
                        # print("*"*10)
                        # print(e)
                        new_element = [e+[i] for i in range(max(e)+1,n)]
                        # print(new_element)
                        # print("*"*10)
                        if new_element:
                            combos+=[e+[i] for i in range(max(e)+1,n)]
                # print("&"*10)
                # print(n,c,combos)
                # print("&"*10)
                
                return combos
        combinations = combinatorics(len(nums),len(nums))
        total = sum(nums)
        for c in combinations:
            new_sum = sum([nums[i] for i in c])

            if new_sum == total-new_sum:
                return True
        return False
                    



            
            
            

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(s):
            pair={")":"("}
            check_stack=[]
            for i in s:
                if i=='(':
                    check_stack.append(i)
                else:
                    check_stack.pop()
            return len(check_stack)==0


        # open_stack=['(']*(n-1)
        # close_stack=[')']*n

        # print("Open Stack: ",open_stack)
        # print("Close Stack: ",close_stack)

        res = ['(']

        target=n*2-1

        while target>0:
            target-=1
            new_res=[]
            for i in range(len(res)):
                if is_valid(res[i]):
                    new_res.append(res[i]+'(')
                else:
                    count=0
                    for c in res[i]:
                        if c=='(':
                            count+=1
                    if count<n:
                        new_res.append(res[i]+'(')
                    new_res.append(res[i]+')')
            res=new_res
            print(new_res)
        return new_res




        
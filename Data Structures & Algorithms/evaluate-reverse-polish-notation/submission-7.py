class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # operators = ['+','-','*','/']
        # for token in tokens:
        #     # print(stack)
        #     if token not in operators:
        #         stack.append(int(token))
        #     else:
        #         a = stack.pop()
        #         b = stack.pop()
        #         if token=='+':
        #             stack.append(a+b)
        #         elif token=='-':
        #             stack.append(a-b)
        #         elif token=='*':
        #             stack.append(a*b)
        #         elif token=='/':
        #             stack.append(int(b/a))
        # return stack[-1]

        # Tree approach
        def dfs():
            token = tokens.pop()
            if token not in  "+-*/":
                return int(token)
            a = dfs()
            b = dfs()

            if token=='+':
                return a+b
            elif token=='-':
                return b-a
            elif token=='*':
                return a*b
            elif token=='/':
                return int(b/a)
        
        return dfs()
            
            


        
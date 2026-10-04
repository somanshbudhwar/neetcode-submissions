class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','/','*']
        stack = []

        for t in tokens:
            print(stack)
            if t not in operators:
                stack.append(int(t))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if t=='+':
                    stack.append(num1+num2)
                elif t=='-':
                    stack.append(num2-num1)
                elif t=='/':
                    stack.append(int(num2/num1))
                elif t=='*':
                    stack.append(int(num1*num2))
        return stack[-1]


        
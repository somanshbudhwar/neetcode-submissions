class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res = [0]*len(temperatures)
        for index,temperature in enumerate(temperatures):
            if not stack:
                stack.append([temperature,index,0,0])
                continue
            if temperature<=stack[-1][0]:
                stack.append([temperature,index,0,0])
            else:
                new_element=[temperature,index,0,0]
                while stack and temperature>stack[-1][0]:
                    stack[-1][-2]+=new_element[-1]+1
                    popped_temp = stack.pop()
                    res[popped_temp[1]]=popped_temp[2]
                    new_element[-1]+=1+popped_temp[3]
                stack.append(new_element)
                print(stack)
        return res

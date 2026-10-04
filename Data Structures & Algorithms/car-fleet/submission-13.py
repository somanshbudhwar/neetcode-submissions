class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joint_array = [(s,p) for s,p in zip(speed,position)]
        joint_array.sort(key=lambda x:x[1])
        print(joint_array)

        steps_needed = [(target-p)/s for s,p in joint_array]

        res =[]

        for step in reversed(steps_needed):
            if not res:
                res.append(step)
            else:
                if step<=res[-1]:
                    continue
                else:
                    res.append(step)
        print(res)
        return len(res)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # CRITICAL
        joint_array = [(s,p) for s,p in zip(speed,position)]
        joint_array.sort(key=lambda x:x[1])
        print(joint_array)

        # CRITICAL
        time_needed = [(target-p)/s for s,p in joint_array]

        res =[]

        for time in reversed(time_needed):
            if not res:
                res.append(time)
            else:
                if time<=res[-1]:
                    continue
                else:
                    res.append(time)
        print(res)
        return len(res)
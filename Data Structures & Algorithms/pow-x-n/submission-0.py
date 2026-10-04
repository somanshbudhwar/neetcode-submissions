class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        
        res=1
        power=abs(n)
        
        while power:
            if power&1:
                res*=x
                power=power-1
            else:
                x*=x
                power = int(power/2)
        if n<0:
            return 1/res
        return res

        
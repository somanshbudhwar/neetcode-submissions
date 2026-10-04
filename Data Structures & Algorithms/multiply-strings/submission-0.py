class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mp = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        def str_to_int(s):
            n1=0
            digit=1
            for d in reversed(s):
                n1+=digit*mp[d]
                digit*=10
            return n1

        res=str_to_int(num1)*str_to_int(num2)
        print(res)
        return str(res)
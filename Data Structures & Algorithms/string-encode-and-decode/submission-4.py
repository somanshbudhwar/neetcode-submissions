class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=f"|BEGIN|{s}|END|"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        # print(s)
        if s=="|BEGIN||END|":
            return [""]
        res = []
        i=0
        begin=False
        end=False
        temp=""
        while i<len(s):
            # print(i, temp, res)
            if s[i:i+5]=="|END|":
                print("In END",i,temp)
                begin=False
                i+=5
                res.append(temp)
                temp=""
            if s[i:i+7]=="|BEGIN|":
                begin=True
                print("In BEGIN",i,temp)
                i+=7
                continue
            if begin:
                temp+=s[i]
                i+=1
                continue
        return res
            



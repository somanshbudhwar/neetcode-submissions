class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        print(hand)
        mp=[]
        res=[]
        final=[]
        for num in hand:
            print(mp,res)
            if num not in mp:
                mp.append(num+1)
                res.append([num])
            else:
                res[mp.index(num)].append(num)
                mp[mp.index(num)]+=1
            if len(res[mp.index(num+1)])==groupSize:
                final.append(res.pop(mp.index(num+1)))
                mp.pop(mp.index(num+1))
        
        if res:
            return False
        for group in final:
            if len(group)!=groupSize:
                return False
        return True
        
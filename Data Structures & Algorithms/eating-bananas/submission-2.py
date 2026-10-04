class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_simulation(rate):
            hours=0
            for pile in piles:
                rem=pile
                hours+= math.ceil(float(pile)/rate)
            return hours
    
        l=1
        r=max(piles)

        best_rate=r

        while l<=r:
            rate=int((l+r)/2)
            hours = eat_simulation(rate)
            print(l,r,rate,hours)

            if hours<=h:
                r=rate-1
                if rate<best_rate:
                    best_rate=rate
            elif hours>h:
                l=rate+1
            # else:
            #     return rate
        return best_rate



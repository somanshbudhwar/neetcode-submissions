class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for x,y in points:
            distance=math.sqrt(x**2+y**2)
            distances.append((x,y,distance))
        
        k_elements=heapq.nsmallest(k,distances,lambda x:x[-1])
        res=[]
        for element in k_elements:
            res.append([element[0],element[1]])
        return res


        
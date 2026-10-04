class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0

        while l<r:
            curr_area=(r-l)*min(heights[l],heights[r])
            if curr_area>max_area:
                max_area=curr_area
            
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            # print(l,r,curr_area)
        return max_area

        
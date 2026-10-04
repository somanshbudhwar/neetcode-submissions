class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0

        while l<r:
            # if l>0 and heights[l]==heights[l-1]:
            #     continue
            # if r<len(heights)-1 and heights[r]==heights[r+1]:
            #     continue
            curr_area=(r-l)*min(heights[l],heights[r])
            if curr_area>max_area:
                max_area=curr_area
            
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            # print(l,r,curr_area)
        return max_area

        
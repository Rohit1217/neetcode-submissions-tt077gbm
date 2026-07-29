class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start=0
        end=len(heights)-1

        curr_water=min(heights[start],heights[end])*(end-start)
        max_water=curr_water

        while start<end:
            print(start,end,heights[start+1],heights[end-1])
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1

            curr_water=min(heights[start],heights[end])*(end-start)
            max_water=max(max_water,curr_water)
        
        return max_water
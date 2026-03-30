class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        left=0
        right=len(heights)-1

        if heights[left]<heights[right]:
            min_height=heights[left]
            min_height_index=left
        else:
            min_height=heights[right]
            min_height_index=right

        area=(right-left)*(min_height)
        print(right)
        while left<right:
            if min_height_index==left:
                while min_height>=heights[left] and left<=right:
                    left=left+1
            else:
                while min_height>=heights[right] and right>=left:
                    right=right-1
                    # print(right)
            
            if left>=right:
                return area

            if heights[left]<heights[right]:
                min_height=heights[left]
                min_height_index=left
            else:
                min_height=heights[right]
                min_height_index=right

            new_area=(right-left)*(min_height)
            if new_area>area:
                area=new_area

        return area    
            
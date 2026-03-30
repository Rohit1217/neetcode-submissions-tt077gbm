class Solution:
    def maxArea(self,heights):
        if len(heights)<2:
            return 0

        def rec_maxArea(left,right):
            if right-left==1:
                return min(heights[left],heights[right])
            else:
                if heights[left]<heights[right]:
                    min_height=heights[left]
                    left=left+1
                    return max(min_height*(right-left+1),rec_maxArea(left,right))
                else:
                    min_height=heights[right]
                    right=right-1
                    return max(min_height*(right-left+1),rec_maxArea(left,right))
        
        return rec_maxArea(0,len(heights)-1)
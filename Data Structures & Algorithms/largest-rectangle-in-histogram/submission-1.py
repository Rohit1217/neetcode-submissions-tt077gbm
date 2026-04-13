class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        monotonic_stack=[]
        max_area=0
        num_bars=len(heights)
        

        for idx in range(len(heights)):
            curr_val=heights[idx]
            while monotonic_stack and  monotonic_stack[-1][1]>=curr_val:
                _,val=monotonic_stack.pop()
                
                if monotonic_stack:
                    curr_area=val*(idx-monotonic_stack[-1][0]-1)
                else:
                    curr_area=val*(idx)
                    
                if curr_area>max_area:
                    max_area=curr_area

            monotonic_stack.append((idx,curr_val))

        
        while monotonic_stack:
            idx,val=monotonic_stack.pop()
            if monotonic_stack:
                curr_area=val*(num_bars-monotonic_stack[-1][0]-1)
            else:
                curr_area=val*(num_bars)
        
            if curr_area>max_area:
                max_area=curr_area        
        
        return max_area


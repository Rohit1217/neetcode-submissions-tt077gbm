class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n=len(heights)
        next_min=[n]*n
        prev_min=[-1]*n

        stack=[]

        for i in range(0,n):
            while stack and stack[-1][0]>heights[i]:
                _,idx=stack.pop()
                next_min[idx]=i
            
            stack.append((heights[i],i))

        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]>heights[i]:
                _,idx=stack.pop()
                prev_min[idx]=i
            
            stack.append((heights[i],i))

        # print(prev_min,next_min)
        max_area=0
        for i in range(0,n):
            height=heights[i]
            width=next_min[i]-prev_min[i]-1

            max_area=max(max_area,height*width)
        
        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append a 0 to flush out all remaining elements in the stack at the end
        heights.append(0)
        stack = [-1] # Initialize with a dummy index to handle the left boundary easily
        max_area = 0
        
        for i in range(len(heights)):
            # Maintain a monotonically increasing stack
            while stack and stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                # The width is determined by the current index and the new top of the stack
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
            
        return max_area

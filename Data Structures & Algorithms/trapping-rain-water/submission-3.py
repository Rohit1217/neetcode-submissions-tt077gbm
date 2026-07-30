class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left = 0
        right = n - 1
        leftMax = 0
        rightMax = 0
        water = 0

        while left <= right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax <= rightMax:
                water += leftMax - height[left]
                left += 1
            else:
                water += rightMax - height[right]
                right -= 1
        
        return water
class Solution:
    def trap(self, height: List[int]) -> int:

        n=len(height)
        prefix_max=[0]*n
        suffix_max=[0]*n

        

        curr_max=0
        for idx in range(n):
            prefix_max[idx]=curr_max
            curr_max=max(curr_max,height[idx])
        
        curr_max=0
        for idx in range(n-1,-1,-1):
            suffix_max[idx]=curr_max
            curr_max=max(curr_max,height[idx])
        
        count=0
        for idx in range(n):
            count+=max(0,min(prefix_max[idx],suffix_max[idx])-height[idx])
            print(idx,max(0,min(prefix_max[idx],suffix_max[idx])-height[idx]))

        return count    
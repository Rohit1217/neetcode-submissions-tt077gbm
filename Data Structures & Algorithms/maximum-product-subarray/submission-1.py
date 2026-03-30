class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        n=len(nums)
        for i in range(1,n):
            new_max=max(nums[i],nums[i]*curr_max,nums[i]*curr_min)
            curr_min=min(nums[i],nums[i]*curr_max,nums[i]*curr_min)
            curr_max=new_max
            print(curr_max,curr_min)
            if curr_max>res:
                res=curr_max
        return res
            
        
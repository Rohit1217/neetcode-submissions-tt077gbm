class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 

        curr_minm=nums[n-1]
        curr_maxm=nums[n-1]
        res=nums[n-1]

        for i in range(n-2,-1,-1):
            temp=min(nums[i],curr_minm*nums[i],curr_maxm*nums[i])
            curr_maxm=max(nums[i],curr_minm*nums[i],curr_maxm*nums[i])
            curr_minm=temp

            res=max(curr_maxm,res)

        return res




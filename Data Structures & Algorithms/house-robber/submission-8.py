class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0

        if len(nums)<3:
            return max(nums)
        
        n=len(nums)
        succ=max(nums[-1],nums[-2])
        next_succ=nums[-1]

        for idx in range(n-3,-1,-1):
            temp=succ
            succ=max(next_succ+nums[idx],succ)
            next_succ=temp
        
        return succ
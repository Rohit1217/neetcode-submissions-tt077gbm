class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_val=sum(nums)
        
        if sum_val%2==1:
            return False
        
        target=sum_val//2

        memo=[[None for j in range(target+1)] for _ in range(len(nums)+1) ]

        def can_part_rec(i,t):
            if t==0:
                return True

            if i==len(nums) or t<0:
                return False
            
            if memo[i][t] is not None:
                return memo[i][t]
            
            ans=can_part_rec(i+1,t) or can_part_rec(i+1,t-nums[i])

            memo[i][t]=ans

            return ans
        
        return can_part_rec(0,target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n=len(nums)
        if n==0:
            return 0

        sum_nums=sum(nums)
        target=sum_nums/2

        if target!=(sum_nums)//2:
            return False
        else:
            target=sum_nums//2 

        memo = [[-1] * (target + 1) for _ in range(n)]
        
        def subset_target_rec(i,curr_t):
            if curr_t==0:
                return True
            elif i>n-1 or curr_t<0:
                return False    
            elif memo[i][curr_t]!=-1:
                return memo[i][curr_t]
            else:
                memo[i][curr_t]=subset_target_rec(i+1,curr_t) or subset_target_rec(i+1,curr_t-nums[i])            
            return memo[i][curr_t]


        subset_target_rec(0,target)
        return memo[0][target]

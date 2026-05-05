class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        last_allowed=False
        memo=[-1]*n

        def rob_rec(i):
            if i>n-1:
                return 0
            elif i==n-1 and last_allowed==False:
                return 0
            elif memo[i]!=-1:
                return memo[i]
            else:
                memo[i]=max(nums[i]+rob_rec(i+2),rob_rec(i+1))
            
            return memo[i]

        rob_first=nums[0]+rob_rec(2)
        
        memo=[-1]*n
        last_allowed=True
        rob_not_first=rob_rec(1)

        return max(rob_first,rob_not_first)

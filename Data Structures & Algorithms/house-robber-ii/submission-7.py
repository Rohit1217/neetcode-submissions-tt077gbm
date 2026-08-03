class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[None for i in range(n+1)]
        last_allowed=False

        def rob_rec(i):
            if i>n-1:
                return 0
            elif i==n-1 and last_allowed==False:
                return 0
            elif dp[i] is not None:
                return dp[i]
            else:
                dp[i]=max(nums[i]+rob_rec(i+2),rob_rec(i+1))
                return dp[i]
        

        rob0=nums[0]+rob_rec(2)
        last_allowed=True
        
        dp=[None for i in range(n+1)]

        rob1=rob_rec(1)
        return max(rob0,rob1)
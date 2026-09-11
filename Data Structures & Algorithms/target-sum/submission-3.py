class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        dp=[{} for i in range(n)]
        
        def tsum(i,t):
            if t==0 and i==n:
                return 1
            elif i==n:
                return 0
            elif t in dp[i]:
                return dp[i][t]
            else:
                countp=tsum(i+1,t-nums[i])
                countn=tsum(i+1,t+nums[i])
                
                dp[i][t]=countp+countn
            
                return dp[i][t]
        
        return tsum(0,target)



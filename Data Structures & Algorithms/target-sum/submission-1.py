from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        
        dp=defaultdict(lambda: defaultdict(int))
        dp[0][0]=1
        

        for  i in  range(n):
            for sums,counts in dp[i].items():
                dp[i+1][sums+nums[i]]+=counts
                dp[i+1][sums-nums[i]]+=counts

        return dp[n][target]
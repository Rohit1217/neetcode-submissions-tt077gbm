class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2!=0:
            return False
        else:
            target =sum(nums)//2
        

        dp=[False for  i in range(target+1)]
        dp[0]=True

        for num in nums:
            for t in range(target,num-1,-1):
                dp[t]=dp[t] or dp[t-num]

        return dp[target]>0
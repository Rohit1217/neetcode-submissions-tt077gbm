class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[float("inf") for _ in range(amount+1)]

        dp[0]=0

        for c in coins:
            for a in range(c,amount+1):
                dp[a]=min(dp[a],1+dp[a-c])
        
        if dp[amount]==float("inf"):
            return -1

        return dp[amount]


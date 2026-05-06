class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n=len(coins)    
        dp=[[0 for i in range(amount+1)] for j in range(n)]

        for i in range(n):
            dp[i][0]=1

        for i in range(n):
            for j in range(1,amount+1):
                if i-1>-1:
                    dp[i][j]=dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    print(coins[i],dp[i][j-1],i,j)
                    dp[i][j]= dp[i][j-coins[i]]
        
        return dp[-1][-1]


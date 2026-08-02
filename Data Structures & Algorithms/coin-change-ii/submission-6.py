class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        dp=[0 for i in range(amount+1)]
        dp[0]=1

        for c in coins:
            for a in range(1,amount+1):
                if (a-c)>-1:
                    dp[a]=dp[a-c]+dp[a]


        return dp[amount]
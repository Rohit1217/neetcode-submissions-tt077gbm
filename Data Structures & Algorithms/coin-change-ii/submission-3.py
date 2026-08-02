class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()

        dp=[[None for _ in range(amount+1)] for i in range(len(coins))]

        def change_rec(n,c):
            # print(c,len(dp),len(dp[0]),amount,len(coins))
            if n==0:
                return 1
            elif n<0:
                return 0
            elif dp[c][n] is not None:
                return dp[c][n]
            else:
                ans=0
                
                for nc in range(len(coins)):
                    new_coin,old_coin=coins[nc],coins[c]

                    if new_coin<=old_coin:
                      ans+=change_rec(n-new_coin,nc)
                
                dp[c][n]=ans

                return ans
        
        return change_rec(amount,len(coins)-1)
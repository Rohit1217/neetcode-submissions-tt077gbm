class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo=[-1 for i in range(amount+1)]
        minm=min(coins)

        def coinchange_rec(i):
            if i<0 :
                return amount+1
            elif i==0:
                return 0
            elif memo[i]!=-1:
                return memo[i]
            else:
                val=amount+1
                for coin in coins:
                    val=min(val,1+coinchange_rec(i-coin))
                memo[i]=val

            return memo[i] 

        num_changes=coinchange_rec(amount)
        if num_changes>amount:
            return -1
        
        return num_changes
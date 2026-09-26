class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=[None for i in range(amount+1)]
        n=len(coins)


        def coin_rec(t):
            if t==0:
                return 0
            elif t<0:
                return amount+1
            elif memo[t] is not None:
                return memo[t]
            else:
                res=amount+1
                for c in coins:
                    res=min(1+coin_rec(t-c),res)
                
                memo[t]=res
                return res
        
        res=coin_rec(amount)

        if res<=amount:
            return res
        
        return -1
                

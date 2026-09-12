class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        memo=[[None for i in range(amount+1)] for j in range(n)]


        def coin(i,a):
            if a==0:
                return 0
            elif i==n or a<0:
                return float("inf")
            elif memo[i][a] is not None:
                return memo[i][a]
            else:
                min_change=float("inf")
                for j in range(i,n):
                    min_change=min(min_change,1+coin(j,a-coins[j]))
                
                memo[i][a]=min_change
                return min_change
        
        ans=coin(0,amount)
        if ans==float("inf"):
            return -1
        return ans

            



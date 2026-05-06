class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #dp[c][i]=min(dp[c-1][i],1+dp[c-1][i-coin[c]]

        res=[amount+1]*(amount+1)
        parent=[amount+1]*(amount+1)
        n=len(res)-1
        res[0]=0


        for i in range(0,n+1):
            for coin in coins:
                if i-coin>-1:
                    prev=res[i]
                    res[i]=min(res[i],1+res[i-coin])
                    
                    if prev!=res[i]:
                        parent[i]=coin
        
        print(parent)
        if res[amount]==amount+1:
            return -1
        return res[amount]


        







        
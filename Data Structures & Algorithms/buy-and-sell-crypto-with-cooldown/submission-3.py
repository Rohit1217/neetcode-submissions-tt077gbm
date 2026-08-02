class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp=[{True:None,False:None} for _ in range(len(prices))]

        def maxprofit_rec(i,flag):
            if i>=len(prices):
                return 0
            elif dp[i][flag] is not None:
                return dp[i][flag]

            if flag:
                buy=maxprofit_rec(i+1,False) - prices[i]
                skip=maxprofit_rec(i+1,True)
                dp[i][flag]=max(buy,skip)
            else:
                sell=maxprofit_rec(i+2,True) + prices[i]
                skip=maxprofit_rec(i+1,False)
                dp[i][flag]=max(sell,skip)
            
            return dp[i][flag]
        
        return maxprofit_rec(0,True)

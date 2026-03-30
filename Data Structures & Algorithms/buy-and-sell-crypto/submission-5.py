class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        
        curr_max=0
        max_profit=0
        
        for idx in range(n-1,-1,-1):
            profit=curr_max-prices[idx]
            max_profit=max(max_profit,profit)

            curr_max=max(curr_max,prices[idx])
        
        return max_profit

        
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        suffix_max_arr=[0]*n
        
        curr_max=0
        
        for idx in range(n-1,-1,-1):
            suffix_max_arr[idx]=curr_max
            curr_max=max(curr_max,prices[idx])
        
        
        max_profit=0

        for idx in range(n):
            profit=suffix_max_arr[idx]-prices[idx]
            max_profit=max(max_profit,profit)
        
        return max_profit

        
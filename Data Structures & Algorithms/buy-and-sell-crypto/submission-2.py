class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        
        curr_idx=len(prices)-2
        max_profit=0
        curr_max=prices[curr_idx+1]
        
        while curr_idx>-1:
            curr_val=prices[curr_idx]
            curr_profit=curr_max-curr_val
            
            if curr_profit>max_profit:
                max_profit=curr_profit
            
            curr_max=max(curr_val,curr_max)
            curr_idx-=1
        return max_profit

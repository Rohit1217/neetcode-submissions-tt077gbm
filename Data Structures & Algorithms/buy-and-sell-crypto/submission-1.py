class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hash_max={}
        curr_max=-1
        max_profit=0
        for i in range(len(prices)-1):
            j=len(prices)-1-i
            if prices[j]>curr_max:
                curr_max=prices[j]
            curr_profit=curr_max-prices[j-1]
            if curr_profit>max_profit:
                max_profit=curr_profit


        # max_profit=0
        # for i in range(len(prices)-1): 
        #     curr_profit=hash_max[prices[i]]-prices[i]   
        #     if curr_profit>max_profit:
        #         max_profit=curr_profit
        return max_profit


        
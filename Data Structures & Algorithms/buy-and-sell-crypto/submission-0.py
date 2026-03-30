class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hash_max={}
        curr_max=-1
        for i in range(len(prices)-1):
            j=len(prices)-1-i
            if prices[j]>curr_max:
                curr_max=prices[j]
            hash_max[prices[j-1]]=curr_max

        max_profit=0
        for i in range(len(prices)-1): 
            curr_profit=hash_max[prices[i]]-prices[i]   
            if curr_profit>max_profit:
                max_profit=curr_profit
        return max_profit


        
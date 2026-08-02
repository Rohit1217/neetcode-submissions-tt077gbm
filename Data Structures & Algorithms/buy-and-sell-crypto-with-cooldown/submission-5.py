class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dpTrue=[0 for _ in range(len(prices)+3)]
        dpFalse=[0 for _ in range(len(prices)+3)]

        for j in range(len(prices)-1,-1,-1):
            price=prices[j]

            dpTrue[j]=max(dpFalse[j+1]-price,dpTrue[j+1])
            dpFalse[j]=max(dpTrue[j+2]+price,dpFalse[j+1])    
        
        return dpTrue[0]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def is_local_max(idx):
            if idx==0:
                if prices[idx+1]<prices[idx]:
                    return True
            elif idx==len(prices)-1:
                if prices[idx]>=prices[idx-1]:
                    return True
            elif prices[idx]>=prices[idx-1] and prices[idx]>prices[idx+1]:
                return True
            return False

        def is_local_min(idx):
            if idx==0:
                if prices[idx+1]>prices[idx]:
                    return True
            elif idx==len(prices)-1:
                if prices[idx]<=prices[idx-1]:
                    return True
            elif prices[idx]<=prices[idx-1] and prices[idx]<prices[idx+1]:
                return True
            return False

        val=0
        buy_idx=0
        for idx in range(len(prices)):
            if is_local_max(idx):
                print(idx,buy_idx)
                val+= prices[idx]-prices[buy_idx] 
            
            if is_local_min(idx):
                buy_idx=idx
                
        return val
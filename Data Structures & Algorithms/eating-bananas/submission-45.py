import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        n=len(piles)

        def timetoFinish(k):
            total_time=0
            for i in range(n):
                total_time+=math.ceil(piles[i]/k)

            return total_time        

        left=1
        right=max(piles)+1

        if h<len(piles):
            return -1
        
        while left<right:
            mid=(left+right)//2

            time_mid=timetoFinish(mid)
            
            if time_mid>h:
                left=mid+1
            else:
                right=mid

        if left>right:
            return right
        return left


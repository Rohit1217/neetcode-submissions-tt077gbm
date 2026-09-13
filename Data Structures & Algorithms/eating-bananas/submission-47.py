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
        right=max(piles)

        # ans in range [left,right)

        if h<len(piles):
            return -1
        
        # Either answer in arr or answer among one last left,right
        while left!=right: #condition when no valid index left (left,left) form
            mid=(left+right)//2
            
            time_mid=timetoFinish(mid)
            
            if time_mid>h:
                left=mid+1 #answer in left half [mid+1,right]
            else:
                right=mid #Answer in [left,mid] mid can also be the answer but we want to find smaller value

        return left


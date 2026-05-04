class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_finish_time(k):
            finish_time=0
            for pile in piles:
                finish_time+= pile//k
                if pile%k!=0:
                    finish_time+=1
            return finish_time
        
        left=1
        right=max(piles)
        
        while left<=right:
            mid=(left+right)//2
            mid_f_time=get_finish_time(mid)
            
            if mid_f_time<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        
        return left




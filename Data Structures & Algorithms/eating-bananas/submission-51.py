
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #RAMANDE VACHISWA

        n=len(piles)
        
        if h<n:
            return -1

        def time_to_eat(speed):
            time=0
            for pile in piles:
                time+=math.ceil(pile/speed)
            
            return time
        
        left=1
        right=max(piles) #include l,r
        mid=(left+right)//2    


        while left<right:
            # print(left,right)
            mid=(left+right)//2    
            
            time=time_to_eat(mid)
            
            if time<=h:
                right=mid-1
            else:
                left=mid+1

        if time_to_eat(max(1,left-1))<=h:
            return max(1,left-1)            

        if time_to_eat(left)<=h:
            return left
        
        if time_to_eat(left+1)<=h:
            return left+1
                        


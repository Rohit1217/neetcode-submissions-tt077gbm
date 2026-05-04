class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Given integer array piles piles[i] num bananans in ith pile
        #Given h number of hours to eat all bananans
        #We can choose per hour eating rate k. Choose pile in one hour finish k banana in pile
        # if num banana less than k in pile then finish pile
        # Return min k

        #Need to find finish time for a given k first
        #Finish time monotonic,ordered in k can do binary search
        #find min k such that finish time less than k
        

        def get_finish_time(k):
            finish_time=0
            for pile in piles:
                finish_time+= pile//k
                if pile%k!=0:
                    finish_time+=1
            return finish_time
        

        left=1
        right=max(piles)
        ans=max(piles)
        
        while left<right:
            mid=(left+right)//2
            mid_f_time=get_finish_time(mid)
            
            if mid_f_time==h:
                if mid<ans:
                    ans=mid
                
                right=mid-1

            elif mid_f_time<h:
                right=mid-1
            else:
                left=mid+1

        if get_finish_time(left)>h and ans>left+1:
            return left+1
        elif get_finish_time(left)<=h and ans>left:
            return left
        
        return ans




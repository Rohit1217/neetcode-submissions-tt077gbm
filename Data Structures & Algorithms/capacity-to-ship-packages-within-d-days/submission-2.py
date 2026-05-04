class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def num_days(capacity):
            num_days=1
            curr_capacity=capacity
            
            for weight in weights:
                if curr_capacity<weight:
                    curr_capacity=capacity
                    num_days+=1
                    
                curr_capacity-=weight            
            return num_days
        
        left,right=max(weights),sum(weights)
        
        while left<right:
            mid=(left+right)//2

            num_days_mid=num_days(mid)
            if num_days_mid<=days:
                right=mid
            else:
                left=mid+1
        
        return left
            

        

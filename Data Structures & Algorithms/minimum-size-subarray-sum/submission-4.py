class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        end=0
        n=len(nums)

        res=n+1
        running_sum=0

        while end<n:
            running_sum+=nums[end]
            
            while running_sum>=target :
                res=min(end-start+1,res)
                running_sum-=nums[start]
                start+=1

            end+=1
                    
        if res>n:
            return 0

        return res
        
        
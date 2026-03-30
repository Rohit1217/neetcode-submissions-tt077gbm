class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        if 1 not in nums:
            return 1

        curr_idx=0        
        for idx in range(len(nums)):
            curr_idx=idx
            val=nums[curr_idx]
            next_idx=val-1

            while -1<next_idx<n and next_idx!=curr_idx:
                curr_idx=next_idx
               
                new_val=nums[curr_idx]                
                nums[next_idx]=val
                
                val=new_val
                next_idx=new_val-1

        ans=1
        for idx in range(len(nums)):
            if nums[idx]!=ans:
                return ans
            ans+=1

        return ans


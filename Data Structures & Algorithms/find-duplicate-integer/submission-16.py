class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast_ptr=0
        slow_ptr=0

        for i in range(len(nums)+1):            
            if nums[fast_ptr]==-1:
                return fast_ptr

            prev=fast_ptr
            fast_ptr=nums[fast_ptr]
            nums[prev]=-1
        

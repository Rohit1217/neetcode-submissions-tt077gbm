class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        
        left=0
        right=len(nums)-1

        while left<=right:
            
            mid=(left+right)//2
            val=nums[mid]
            print(left,right,mid)
            if target==val:
                return mid
            
            elif nums[left]<=val:
                if target<val and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            
            else:
                if target>val and target<=nums[right]:
                    left=mid+1    
                else:
                    right=mid-1
        
        return -1
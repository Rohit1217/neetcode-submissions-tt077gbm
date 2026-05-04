class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left,right=0,n-1

        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        
        r_idx=left

        left,right=0,n-1

        while left<right:
            mid=(left+right)//2
            r_mid=(mid+r_idx)%n

            if nums[r_mid]==target:
                return r_mid
            elif nums[r_mid]<target:
                left=mid+1
            else:
                right=mid
        
        if nums[(left+r_idx)%n]==target:
            return (left+r_idx)%n
        
        return -1
            
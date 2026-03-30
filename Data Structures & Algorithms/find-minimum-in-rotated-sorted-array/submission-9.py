class Solution:
    def findMin(self,nums):
        if len(nums)==0:
            return -1
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[right]
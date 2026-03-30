class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        if nums[0]>nums[-1]<nums[-2]:
            return nums[-1]
        elif nums[-1]>nums[0]<nums[1]:
            return nums[0]
        
        left=0
        right=len(nums)-1

        while (right-left)>1:
            mid=(left+right)//2
            if nums[mid-1]>nums[mid]<nums[mid+1]:
                return nums[mid]
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid-1
        return min(nums[left],nums[right])
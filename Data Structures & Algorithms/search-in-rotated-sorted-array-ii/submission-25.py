class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left=0
        right=len(nums)-1

        if nums[right]==target:
            return True

        while left<=right:
            print(left,right,nums[left],nums[right])
            mid=(left+right)//2

            if nums[mid]==target:
                return True

            if nums[left]==nums[mid]:
                left+=1
            elif nums[mid]==nums[right]:
                right-=1
            
            elif nums[left]<nums[right]:
                if target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            
            elif nums[left]<nums[mid]: # If mid>left left half sorted
                if target>nums[right]:  #if target>right it is in left else right
                    right=mid-1
                else:
                    left=mid+1

            elif nums[mid]<nums[right]:
                if target<nums[right] and target>nums[mid]: 
                    left=mid+1
                else:
                    right=mid-1
        
        return False

            
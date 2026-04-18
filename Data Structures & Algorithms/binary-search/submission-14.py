class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        left,right=0,len(nums)-1

        while (left<right):
            search_idx=(left+right)//2
            
            if nums[search_idx]<target:
                left=search_idx+1
            elif nums[search_idx]>target:
                right=search_idx-1
            else:
                return search_idx

        if nums[left]==target:
            return left

        return -1    


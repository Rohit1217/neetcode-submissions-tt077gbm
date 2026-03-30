class Solution:
    def search(self, nums: List[int], target: int) -> int:
        search_index=len(nums)//2
        left,right=0,len(nums)-1
        while right-left>1 :
            if nums[search_index]==target:
                return search_index
            elif nums[search_index]>target:
                right=search_index
            else:
                left=search_index

            search_index=(right+left+1)//2
          
        
        if nums[search_index]==target: 
            return search_index
        elif nums[search_index-1]==target:
            return search_index-1
        
        return -1
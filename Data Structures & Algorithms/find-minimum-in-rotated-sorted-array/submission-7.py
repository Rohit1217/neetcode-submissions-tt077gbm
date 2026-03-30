class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)
        if right-left==1:
            return nums[left]
        if nums[left]<nums[right-1]:
            return nums[left]

        while (right-left)>2:
            search_idx=(left+right)//2
            val=nums[search_idx]
            left_val=nums[search_idx-1]
            right_val=nums[search_idx+1]

            if val<left_val:
                if val<right_val:
                    return nums[search_idx]
                else:
                    left=search_idx+1
            else:
                if val>right_val:
                    return nums[search_idx+1]
                elif val<nums[left]:
                    right=search_idx
                else:
                    left=search_idx+1
        search_idx=left

        if nums[search_idx]>nums[search_idx+1]:
            return nums[search_idx+1]
        else:
            return nums[search_idx]


class Solution:
    def findMinIdx(self, nums: List[int]) -> int:
        left,right=0,len(nums)
        if right-left==1:
            return left
        if nums[left]<nums[right-1]:
            return left

        while (right-left)>2:
            search_idx=(left+right)//2
            val=nums[search_idx]
            left_val=nums[search_idx-1]
            right_val=nums[search_idx+1]

            if val<left_val:
                if val<right_val:
                    return search_idx
            else:
                if val>right_val:
                    return search_idx+1
                elif val<nums[left]:
                    right=search_idx
                else:
                    left=search_idx+1
        search_idx=left

        if nums[search_idx]>nums[search_idx+1]:
            return search_idx+1
        else:
            return search_idx




    def search(self, nums: List[int], target: int) -> int:
        min_idx=self.findMinIdx(nums)
        k=min_idx
        left=0
        right=len(nums)
        print(k)
        if len(nums)==1:
            if nums[left]==target:
                return left
            return -1

        while (right-left)>1:
            search_idx=(left+right)//2
            search_rot_idx=(search_idx+k)%(len(nums))
            if nums[search_rot_idx]==target:
                return search_rot_idx
            elif nums[search_rot_idx]<target:
                left=search_idx+1
            else:
                right=search_idx
        print(left,right)
        if nums[(left+k)%(len(nums))]==target:
            return (left+k)%(len(nums))

        return -1

        
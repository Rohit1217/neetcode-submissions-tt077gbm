class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr_index=0
        if nums[0]==nums[1]:
            return nums[0]
        for i in range(len(nums)):
            next_index=nums[curr_index]
            print(curr_index,next_index,nums[next_index])
            if nums[next_index]==-1 or (curr_index==next_index):
                return next_index
            nums[curr_index]=-1
            curr_index=next_index
        # return curr_index
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pointer=0
        
        for idx in range(len(nums)):
            if nums[idx]==val:
                pass
            else:
                nums[write_pointer]=nums[idx]
                write_pointer+=1
        
        return write_pointer
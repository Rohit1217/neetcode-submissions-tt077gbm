class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_val_pos = {}
       
        for pos in range(len(nums)):
            array_val_pos[nums[pos]] = pos

        for pos in range(len(nums)):
            val = target - nums[pos]
            if val in array_val_pos:
                if array_val_pos[val] != pos:
                    return [pos,array_val_pos[val]]
        

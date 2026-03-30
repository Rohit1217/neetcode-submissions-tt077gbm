class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_hash={}

        for i in range(len(nums)):
            num=nums[i]
            new_target=target-num
            if new_target not in target_hash.keys():
                target_hash[num]=i
            else:
                return [target_hash[new_target],i]
        return
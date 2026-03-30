class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        presence_hash={}
        
        for idx in range(len(nums)):
            presence_hash[nums[idx]]=idx
        
        for idx in range(len(nums)):
            val=nums[idx]
            if target-val in presence_hash and presence_hash[target-val]>idx:
                return [idx,presence_hash[target-val]]
        
        return []

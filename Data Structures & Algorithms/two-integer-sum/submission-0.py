class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            hash[nums[i]]=[1,i]

        for i in range(len(nums)):
            try:
                if hash[target-nums[i]][0]==1 and hash[target-nums[i]][1]!=i:
                    return [i,hash[target-nums[i]][1]]
            except Exception as e:
                continue 
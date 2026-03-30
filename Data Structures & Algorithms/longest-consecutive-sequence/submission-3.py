
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        maxm=1
        hash_table={}
        nums=sorted(nums)
        for i in range(len(nums)):
            try:
                if hash_table[nums[i]-1]==maxm:
                    maxm+=1
                hash_table[nums[i]]= hash_table[nums[i]-1]+1
            except Exception as e:
                hash_table[nums[i]]=1
                continue
        return maxm
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for num in nums:
            hash[num]=0
        for num in nums:
            if hash[num]==1:
                return True
            else:
                hash[num]+=1
        return False
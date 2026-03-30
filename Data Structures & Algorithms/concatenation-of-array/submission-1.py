class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*(n)*2
        
        for idx in range(n):
            val=nums[idx]
            res[idx]=val
            res[idx+n]=val

        return res
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo=[-1]*len(nums)
        n=len(nums)

        def rob_rec(i):
            if i>n-1:
                return 0
            elif memo[i]!=-1:
                return memo[i]
            else:
                memo[i]=max(nums[i]+rob_rec(i+2),rob_rec(i+1))
            
            return memo[i]
        
        return rob_rec(0)
        
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo=[None for j in range(target+1)]
        n=len(nums)

        def combsum_rec(t):
            if t==0:
                return 1
            elif t<0:
                return 0
            elif memo[t] is not None:
                return memo[t]
            else:
                comb_sum=0
                for num in nums:
                    comb_sum+=combsum_rec(t-num)
                
                memo[t]=comb_sum
            
            return memo[t]
        
        return combsum_rec(target)


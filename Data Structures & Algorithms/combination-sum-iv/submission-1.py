class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        memo=[-1]*(target+1)
        
        def comb_sum_rec(t):
            if t<0:
                return 0
            elif t==0:
                return 1
            elif memo[t]!=-1:
                return memo[t]
            else:
                memo[t]=0
                for num in nums:
                    memo[t]+=comb_sum_rec(t-num)
                
            return memo[t]
        

        return comb_sum_rec(target)
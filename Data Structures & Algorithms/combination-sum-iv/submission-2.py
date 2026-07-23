class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo=[None for _ in range(target+1)]

        def comb_sum_rec(i):
            if i<0:
                return 0
            if i==0:
                return 1
            if memo[i] is not None:
                return memo[i]

            comb_sum=0

            for num in nums:
                comb_sum+=comb_sum_rec(i-num)
            
            memo[i]=comb_sum

            return memo[i]
        
        return comb_sum_rec(target)
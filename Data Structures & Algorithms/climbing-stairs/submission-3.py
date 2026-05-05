class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo=[-1]*n

        def climb_rec(i):

            if i==n-2:
                return 2
            elif i==n-1:
                return 1
            elif i>n-1:
                return 0
            elif memo[i]!=-1:
                return memo[i]
            else:
                memo[i]=climb_rec(i+1)+climb_rec(i+2)

            return memo[i]
        
        return climb_rec(0)
        
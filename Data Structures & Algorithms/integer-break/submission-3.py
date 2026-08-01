class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n==1 or n==2:
            return 1

        memo=[None for i in range(n+1)]
        memo[0],memo[1],memo[2]=1,1,2

        def int_break(n):
            if n==0 or n==1:
                return 1
            elif n<0:
                return float("-inf")
            elif memo[n] is not None:
                return memo[n]
            else:
                res=float("-inf")
                
                for i in range(1,n+1):
                    res=max(res,i*int_break(n-i))

                memo[n]=res
                return memo[n]
        
        res=float("-inf")
        for i  in range(n):
            res=max(res,i*int_break(n-i))

        return res
        
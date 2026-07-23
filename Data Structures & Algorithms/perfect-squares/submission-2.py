
import sys

# 1. Check the current recursion limit (usually 1000)
print(sys.getrecursionlimit())

# 2. Set a higher recursion depth limit
sys.setrecursionlimit(50000)
import math
class Solution:
    def numSquares(self, n: int) -> int:
        
        perf_sqr_list=[]
        upper=math.ceil(math.sqrt(n))

        for i in range(1,upper+1):
            perf_sqr_list.append(i*i)


        memo=[None for _ in range(n+1)]

        def num_sq_rec(i):
            if i==0:
                return 0
            if i<0:
                return float("inf")
            
            if memo[i] is not None:
                return memo[i]
            
            minm=float('inf')

            for num in perf_sqr_list:
                minm=min(minm,1+num_sq_rec(i-num))
            
            memo[i]=minm
            return memo[i]

        return num_sq_rec(n)
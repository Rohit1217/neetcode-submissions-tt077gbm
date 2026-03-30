class Solution:

    def climbStairs(self, n: int) -> int:
        self.memo=[-1  for _ in range(n+1) ]
        def climbStairs_memo(n):
            # print(n,len(self.memo))
            if self.memo[n]!=-1:
                return self.memo[n]
            if n==2:
                return 2
            elif n==1:
                return 1
            elif n==0:
                return 0
            else:
                self.memo[n]=climbStairs_memo(n-1)+climbStairs_memo(n-2)
                return self.memo[n]
        return climbStairs_memo(n)
        
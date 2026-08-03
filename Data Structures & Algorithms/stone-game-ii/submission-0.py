class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp = [[None for i in range(n + 1)] for _ in range(n + 1)] 

        def stone_rec(i,m):
            if i>=n:
                return 0
            elif dp[i][m] is not None:
                return dp[i][m]
            else:
                res=float("-inf")
                
                for j in range(i+1,i+1+2*m):
                    if j>n:
                        continue
                    else:
                        res=max(res,sum(piles[i:])-stone_rec(j,max(m,j-i)))
                
                dp[i][m]=res
                return res
        
        stone_rec(0,1)
        print(dp)
        return dp[0][1]

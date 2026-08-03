class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n=len(piles)
        dp=[[None for  i in range(n)] for j in range(n)]

        def stone_rec(i,j):
            if i>j:
                return 0
            elif dp[i][j] is not None:
                return dp[i][j]
            else:
                ans=max(-stone_rec(i,j-1)+piles[j],-stone_rec(i+1,j)+piles[i])
                dp[i][j]=ans
                return ans
        

        return stone_rec(0,n-1)>0

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)

        memo=[[None for i in range(n)] for j in range(n)]

        def stone_rec(i,j):
            if i==j:
                return piles[i]
            elif memo[i][j] is not None:
                return memo[i][j]
            else:
                max_pile=0
                max_pile=max(max_pile,piles[i]-stone_rec(i+1,j))
                max_pile=max(max_pile,piles[j]-stone_rec(i,j-1))

                memo[i][j]=max_pile
            return max_pile
        
        return stone_rec(0,n-1)>0




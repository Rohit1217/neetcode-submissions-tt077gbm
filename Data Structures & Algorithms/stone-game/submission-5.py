class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        # 1. Build the prefix sum array
        prefix = [0] * n
        prefix[0] = piles[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + piles[i]
            
        dp = [[None for _ in range(n)] for _ in range(n)]

        # 2. Optimized range sum lookup
        def get_range_sum(i, j):
            if i > j: 
                return 0
            return prefix[j] if i == 0 else prefix[j] - prefix[i - 1]


        def game_rec(i,j):
            if i>j:
                return 0
            
            elif dp[i][j] is not None:
                return dp[i][j]
            
            else:
                ans=max(-game_rec(i,j-1)+piles[j]+get_range_sum(i,j-1),-game_rec(i+1,j)+piles[i]+get_range_sum(i+1,j))
            dp[i][j]=ans

            return dp[i][j]
        
        alice_sum=game_rec(0,n-1)

        if alice_sum>=(sum(piles)-alice_sum):
            return True
        
        return False
from typing import List

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

        # 3. Your exact mathematical recursion
        def game_rec(i, j):
            if i > j:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]
            
            # Your exact formulas, streamlined
            opt1 = -game_rec(i, j - 1) + piles[j] + get_range_sum(i, j - 1)
            opt2 = -game_rec(i + 1, j) + piles[i] + get_range_sum(i + 1, j)
            
            dp[i][j] = max(opt1, opt2)
            return dp[i][j]
        
        alice_sum = game_rec(0, n - 1)
        total_sum = prefix[-1]
        
        return alice_sum > (total_sum - alice_sum)

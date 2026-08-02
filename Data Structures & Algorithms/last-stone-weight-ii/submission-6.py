class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        stones.sort()
        target=sum(stones)//2

        dp=[False for _ in range(target+1)]
        dp[0]=True

        print(target)

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        
        for i in range(target,-1,-1):
            if dp[i]==True:
                return sum(stones)-2*i
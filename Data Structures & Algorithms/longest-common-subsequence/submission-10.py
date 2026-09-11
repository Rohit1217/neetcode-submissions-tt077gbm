class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m,n=len(text1),len(text2)

        # dp[i][j]=max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])

        dp=[0 for i in range(n)]

        for i in range(0,m):
            prev=0
            for j in range(0,n):
                if text1[i]==text2[j]:
                    res=prev+1
                else:
                    res= max(dp[j], dp[j-1] if j > 0 else 0)

                
                prev=dp[j]
                dp[j]=res
        
        return dp[-1]



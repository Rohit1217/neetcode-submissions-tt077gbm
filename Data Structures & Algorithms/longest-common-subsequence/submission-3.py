class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j]=1+dp[i-1][j-1] or max(dp[i-1][j],dp[i][j-1])
        m,n=len(text1),len(text2)

        lcs=[0 for _ in range(n+1)]

        for i in range(0,m):
            prev=0
            for j in range(0,n):
                if text1[i]==text2[j]:
                    res=max(1+prev,lcs[j],lcs[j+1])
                else:
                    res=max(lcs[j],lcs[j+1])
                
                prev,lcs[j+1]=lcs[j+1],res

        return lcs[n]
                
                
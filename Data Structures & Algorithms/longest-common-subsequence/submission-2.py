class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)

        #dp[i][j]=max(dp[i-1][j],dp[i][j-1],1+dp[i-1][j-1] if s[i]==s[j])

        lcs=[0]*(n+1)

        for i in range(m):
            prev=0
            for j in range(1,n+1):
                if text1[i]==text2[j-1]:
                    res=max(lcs[j],lcs[j-1],1+prev)
                    prev=lcs[j]
                    lcs[j]=res
                else:
                    res=max(lcs[j],lcs[j-1])
                    prev=lcs[j]
                    lcs[j]=res
            
        return lcs[n]
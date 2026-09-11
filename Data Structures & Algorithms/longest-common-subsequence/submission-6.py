class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m,n=len(text1),len(text2)
        memo=[[None for  j in range(n+1)] for i in range(m+1)]

        def lcs(i,j):
            if i==-1 or j==-1:
                return 0
            elif memo[i][j] is not None:
                return memo[i][j]
            else:
                if text1[i]==text2[j]:
                    memo[i][j]=1+lcs(i-1,j-1)
                else:
                    memo[i][j]=max(lcs(i-1,j),lcs(i,j-1))
                
                return memo[i][j]
        
        return lcs(m-1,n-1)

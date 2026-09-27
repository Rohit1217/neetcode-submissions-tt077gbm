class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m,n=len(text1),len(text2)
        memo=[[None for i in range(n)] for j in range(m)]

        def lcs(i,j):
            if i==-1 or j==-1:
                return 0
            elif memo[i][j] is not None:
                return memo[i][j]
            else:
                res=0
                if text1[i]==text2[j]:
                    res+=1+lcs(i-1,j-1)
                else:
                    res=max(lcs(i-1,j),lcs(i,j-1))
                
                memo[i][j]=res
                return res
        
        return lcs(m-1,n-1)
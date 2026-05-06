class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m,n=len(s1),len(s2)

        if n==0:
            return s1==s3
        elif m==0:
            return s2==s3

        if len(s1)+len(s2)!=len(s3):
            return False

        dp=[[False]*(n+1) for _ in range(m+1)]


        if s3[0]==s1[0]:
            dp[1][0]=True

        if s3[0]==s2[0]:
            dp[0][1]=True
        
        for i in range(0,m+1):
            for j in range(0,n+1):

                if s2[j-1]==s3[i+j-1] and j-1>-1:
                    dp[i][j]=dp[i][j] or dp[i][j-1]
                if s1[i-1]==s3[i+j-1] and i-1>-1 :
                    dp[i][j]=dp[i][j] or dp[i-1][j]
                
        print(dp)        
        return dp[-1][-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m,n=len(s),len(t)

        dp=[[None for i in range(n)] for j in range(m)]

        def num_dist(i,j):
            if j==n:
                return 1
            elif i==m:
                return 0
            elif dp[i][j] is not None:
                return dp[i][j]
            else:
                count=0
                if s[i]==t[j]:
                    count=num_dist(i+1,j+1)+num_dist(i+1,j)
                else:
                    count=num_dist(i+1,j)
                
                dp[i][j]=count
            
            return count
        
        return num_dist(0,0)

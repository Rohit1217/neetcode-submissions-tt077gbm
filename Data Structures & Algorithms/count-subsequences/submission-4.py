class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m,n=len(s),len(t)

        dp=[[None for i in range(n+1)] for j in range(m+1)]

        def num_dist(i,j):
            if j<0 :
                return 1
            elif i<0:
                return 0
            elif dp[i][j] is not None:
                return dp[i][j]
            else:
                count=0
                if s[i]==t[j]:
                    count=num_dist(i-1,j-1)+num_dist(i-1,j)
                else:
                    count=num_dist(i-1,j)
                
                dp[i][j]=count
            
            return count
        
        return num_dist(m-1,n-1)
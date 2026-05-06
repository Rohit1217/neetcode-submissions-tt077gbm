class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m,n=len(word1),len(word2)

        memo=[[-1]*n for i in range(m)]

        def min_dist_rec(i,j):
            if i==-1:
                return j+1
            elif j==-1:
                return i+1
            elif memo[i][j]!=-1:
                return memo[i][j]
            else:
                if word1[i]==word2[j]:
                    memo[i][j]=min_dist_rec(i-1,j-1)
                else:
                    memo[i][j]=1+min(min_dist_rec(i-1,j),min_dist_rec(i,j-1),min_dist_rec(i-1,j-1))
            
            return memo[i][j]
    
        return min_dist_rec(m-1,n-1)
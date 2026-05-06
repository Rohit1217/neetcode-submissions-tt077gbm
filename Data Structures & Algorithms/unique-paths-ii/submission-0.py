class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        memo=[[-1 ]*n for i in range(m)]

        memo[m-1][n-1]=1

        def unique_path_rec(i,j):
            if i>m-1 or j>n-1:
                return 0
            elif obstacleGrid[i][j]==1:
                return 0
            elif memo[i][j]!=-1:
                return memo[i][j]
            else:
                memo[i][j]=unique_path_rec(i+1,j) + unique_path_rec(i,j+1)

            return memo[i][j]
        

        return unique_path_rec(0,0)

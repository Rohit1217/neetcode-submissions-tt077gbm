class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        num_paths=[0]*(n+1)
        num_paths[1]=1

        for i in range(m):
            for j in range(1,n+1):
                if obstacleGrid[i][j-1]==1:
                    num_paths[j]=0
                else:
                    num_paths[j]=num_paths[j-1]+num_paths[j]
        
        # print(num_paths)
        return num_paths[n]
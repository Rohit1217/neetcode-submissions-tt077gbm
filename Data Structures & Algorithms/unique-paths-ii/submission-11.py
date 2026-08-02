class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid=obstacleGrid

        r,c=len(grid),len(grid[0])
        dist=[0 for _ in range(c) ]

        if grid[0][0]==1:
            return 0
        else:
            dist[0]=1

        for i in range(0,r):
            if grid[i][0]==1:
                dist[0]=0

            for j in range(1,c):
                if grid[i][j]==1:
                    dist[j]=0
                else:
                    dist[j]=dist[j]+dist[j-1]  
                            
        return dist[c-1]
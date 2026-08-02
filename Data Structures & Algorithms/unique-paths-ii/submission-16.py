class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid=obstacleGrid

        r,c=len(grid),len(grid[0])
        dist=[0 for _ in range(c) ]
        dist[0]=1

        for i in range(r):
            for j in range(c): 
                if grid[i][j] == 1:
                    dist[j] = 0  
                elif j > 0:
                    dist[j] = dist[j] + dist[j-1] 

        return dist[c-1]
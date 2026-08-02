from itertools import accumulate
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        r,c=len(grid),len(grid[0])
        dist=list(accumulate(grid[0]))

        for i in range(1,r):
            dist[0]=grid[i][0]+dist[0]
            for j in range(1,c):
                dist[j]=grid[i][j]+min(dist[j],dist[j-1])

            # print(dist)
        return dist[c-1]
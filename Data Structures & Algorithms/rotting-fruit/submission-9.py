from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nr,nc=len(grid),len(grid[0])

        queue=deque()

        for r in range(nr):
            for c in range(nc):
                if grid[r][c]==2:
                    queue.append((r,c,0))
        
        max_time=0

        while queue:
            r,c,t=queue.popleft()


            neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            
            for neighbor in neighbors:
                neigh_r,neigh_c=neighbor
                if neigh_r>-1 and neigh_c>-1 and neigh_r<nr and neigh_c<nc and grid[neigh_r][neigh_c]==1:
                    queue.append((neigh_r,neigh_c,t+1))
                    grid[neigh_r][neigh_c]=2
                    max_time=max(max_time,t+1)
            
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]==1:
                    return -1

        return max_time            

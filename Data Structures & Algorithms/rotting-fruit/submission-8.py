
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        rows,cols=len(grid),len(grid[0])
        queue=deque([])
        visited=set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    queue.append((row,col,0))
        
        while queue:
            r,c,d=queue.popleft()
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]==0 or (r,c) in visited:
                continue

            visited.add((r,c))
            grid[r][c]=-d
            neighbors=((r-1,c,d+1),(r+1,c,d+1),(r,c-1,d+1),(r,c+1,d+1))

            for neighbor in neighbors:
                nr,nc=neighbor[0],neighbor[1]

                if (nr,nc) not in visited:
                    queue.append(neighbor)

        max_time=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return -1
                elif grid[row][col]!=0:
                    max_time=max(max_time,-grid[row][col])
        
        return max_time





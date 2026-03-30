from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # visited=set()
        rows,cols=len(grid),len(grid[0])
        new_grid=[]
        q=deque()

        for i in range(rows):
            new_grid.append([])
            for j in range(cols):
                new_grid[i].append(-1)
                if grid[i][j]==2:
                    q.append((i,j,0))
                    new_grid[i][j]=0
                

        while len(q)>0:
            i,j,d=q.popleft()
            neighbors=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for i_new,j_new in neighbors:
                if  i_new<0 or i_new>rows-1 or j_new<0 or j_new>cols-1 or new_grid[i_new][j_new]!=-1 or grid[i_new][j_new]==0:
                    continue
                else:
                    q.append((i_new,j_new,d+1))
                    new_grid[i_new][j_new]=d+1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and new_grid[i][j]==-1:
                    return -1
        maxm=0
        for i in range(rows):
                maxm=max(maxm,max(new_grid[i]))
        return maxm


        
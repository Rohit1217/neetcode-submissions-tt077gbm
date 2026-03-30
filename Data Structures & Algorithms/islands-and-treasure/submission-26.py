from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited=set()
        rows,cols=len(grid),len(grid[0])
        q=deque()

        def bfs(q):
            while len(q)!=0:
                # print(q)
                i,j,d=q.popleft()
                neighbors=[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
                for i_new,j_new in neighbors:
                    if i_new<0 or j_new<0 or i_new>rows-1 or j_new>cols-1 or (i_new,j_new) in visited or grid[i_new][j_new]==-1:
                        continue
                    elif grid[i_new][j_new]==0:
                        return d+1
                    else:
                        q.append((i_new,j_new,d+1))
                        visited.add((i_new,j_new))
            return 2147483647
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]>0:
                    q.append((i,j,0))
                    visited.add((i,j))
                    d=bfs(q)
                    grid[i][j]=d
                    visited=set()
                    q=deque()
        return




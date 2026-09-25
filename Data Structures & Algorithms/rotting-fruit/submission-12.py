from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows,cols=len(grid),len(grid[0])
        q=deque([])

        visited=set()

        time=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,time))    

        
        while q:
            r,c,t=q.popleft()

            neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

            for neighbor in neighbors:
                nr,nc=neighbor

                if nr==rows or nc==cols or nr<0 or nc<0 or (nr,nc)  in visited or grid[nr][nc]==0 or grid[nr][nc]==2:
                    continue
                
                q.append((nr,nc,t+1))
                time=max(time,t+1)
                visited.add((nr,nc))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    return -1
        
        return time
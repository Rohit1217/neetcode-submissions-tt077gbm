from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])


        if rows==0 or cols==0:
            return 

        queue=deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    queue.append((row,col,0))
        
        visited=set()

        while queue:
            node=queue.popleft()
            r_idx,c_idx,dist=node

            if r_idx<0 or c_idx<0 or r_idx>rows-1 or c_idx>cols-1 or grid[r_idx][c_idx]==-1 or (r_idx,c_idx) in visited:
                continue
            
            grid[r_idx][c_idx]=dist
            visited.add((r_idx,c_idx))

            queue.append((r_idx-1,c_idx,dist+1))
            queue.append((r_idx+1,c_idx,dist+1))
            queue.append((r_idx,c_idx-1,dist+1))
            queue.append((r_idx,c_idx+1,dist+1))
        
        return

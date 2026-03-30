class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited=set()
        num_islands=0
        rows,cols=len(grid),len(grid[0])

        def dfs(v):
            x,y=v
            
            if x<0 or y<0 or y>cols-1 or x>rows-1 or grid[x][y]=="0":
                return

            if v in visited:
                return
            else:
                visited.add(v)

            dfs((x-1,y))
            dfs((x+1,y))
            dfs((x,y-1))
            dfs((x,y+1))

            return 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and (row,col) not in visited:
                    v=(row,col)
                    dfs(v)
                    num_islands+=1

        return num_islands 
            


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        elif len(grid[0])==0:
            return 0
        
        rows,cols=len(grid),len(grid[0])

        visited=set()

        def dfs(node): 
            r_idx,c_idx=node
            
            if node in visited or r_idx<0 or r_idx>rows-1 or c_idx<0 or c_idx>cols-1 or grid[r_idx][c_idx]=="0":
                return
            
            visited.add(node)

            dfs((r_idx-1,c_idx))
            dfs((r_idx+1,c_idx))
            dfs((r_idx,c_idx-1))
            dfs((r_idx,c_idx+1))

            return

        num_islands=0

        for r_idx in range(rows):
            for c_idx in range(cols):
                if (r_idx,c_idx) not in visited and grid[r_idx][c_idx]=="1":
                    dfs((r_idx,c_idx))
                    num_islands+=1

        return num_islands
        
        


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def dfs(pos):
            r,c=pos

            visited.add(pos)

            neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

            for neighbor in neighbors:
                r,c=neighbor    
                if r<0 or c<0 or r==rows or c==cols or (r,c) in visited or grid[r][c]=="0":
                    continue
                dfs((r,c))
            
        count=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs((r,c))
                    count+=1
        # print(visited)
        return count
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        rows,cols=len(grid),len(grid[0])
        num_islands=0

        def dfs(row,col):
            if row==rows or col==cols or row<0 or col<0 or (row,col) in visited or grid[row][col]=="0":
                return

            visited.add((row,col))

            neighbors=((row-1,col),(row+1,col),(row,col-1),(row,col+1))

            for neighbor in neighbors:
                dfs(neighbor[0],neighbor[1])

            return


        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col]=="1":
                    dfs(row,col)
                    num_islands+=1
        

        return num_islands


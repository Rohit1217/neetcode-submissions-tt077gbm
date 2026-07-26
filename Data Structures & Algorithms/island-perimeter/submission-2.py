class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        perimeter=0

        def add_perim(row,col):
            if row<0 or col<0:
                return 1
            if row==rows or col==cols:
                return 1
            
            if grid[row][col]==0:
                return 1
            return 0

        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col]==1:
                    neighbors=(row-1,col),(row+1,col),(row,col-1),(row,col+1)
                    for neighbor in neighbors:
                        perimeter+=add_perim(neighbor[0],neighbor[1])


        return perimeter


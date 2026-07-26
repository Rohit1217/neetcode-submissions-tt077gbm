class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        rows,cols=len(grid),len(grid[0])
        max_area=0

        def dfs(row,col):
            if row==rows or col==cols or row<0 or col<0 or (row,col) in visited or grid[row][col]==0:
                return 0

            visited.add((row,col))
            area=1

            neighbors=((row-1,col),(row+1,col),(row,col-1),(row,col+1))

            for neighbor in neighbors:
                area+=dfs(neighbor[0],neighbor[1])

            return area


        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col]==1:
                    area=dfs(row,col)
                    max_area=max(max_area,area)
        

        return max_area

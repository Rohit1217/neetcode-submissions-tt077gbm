class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        rows,cols=len(grid),len(grid[0])
        if rows==0:
            return 0
        component=[]
        for i in range(rows):
            component.append([])
            for j in range(cols):
                component[i].append(0)
        
        
        def dfs_2d(pos,counter):
            i,j=pos
            if i>rows-1 or i<0 or j>cols-1 or j<0 or (i,j) in visited or grid[i][j]==0:
                return
            visited.add(pos)
            component[i][j]=counter
            dfs_2d((i,j-1),counter)
            dfs_2d((i+1,j),counter)
            dfs_2d((i,j+1),counter)
            dfs_2d((i-1,j),counter)
            counter+=1
            return counter
        
        counter=1
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]!=0:
                    counter=dfs_2d((i,j),counter)
        
        count_l=[0]*counter  
        # print(component)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0:
                    count_l[component[i][j]]+=1
        print(count_l)                              
        return max(count_l)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited={}
        for i in range(len(grid)):
             visited[i]={}
             for j in range((len(grid[0]))):
                 visited[i][j]=False

        def DFS_2d(grid,visited,pos,counter):
            i,j=pos
            visited[i][j]=True
            if i-1>-1 and grid[i-1][j]=='1' and not visited[i-1][j]:
                DFS_2d(grid,visited,(i-1,j),counter)
            if j-1>-1 and grid[i][j-1]=='1' and not visited[i][j-1]:
                DFS_2d(grid,visited,(i,j-1),counter)
            if j+1<len(grid[0]) and grid[i][j+1]=='1' and not visited[i][j+1]:
                DFS_2d(grid,visited,(i,j+1),counter)
            if i+1<len(grid) and grid[i+1][j]=='1' and not visited[i+1][j]:
                DFS_2d(grid,visited,(i+1,j),counter)    
            grid[i][j]=counter
            counter+=1
            return counter
        
        counter=1
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j]=='1' and not visited[i][j]:
                    print(True)
                    pos=i,j
                    counter=DFS_2d(grid,visited,pos,counter)
        
        l=[]
        print(grid,visited)             
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j]!='0':
                    l.append(grid[i][j])
        l=list(set(l))
        return len(l)
        
       
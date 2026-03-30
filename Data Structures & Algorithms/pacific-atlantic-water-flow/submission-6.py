class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited=set()
        rows,cols=len(heights),len(heights[0])


        def dfs(v,par_height):
            x,y=v
            
            if v in visited or x<0 or y<0 or x>rows-1 or y >cols-1:
                return

            curr_height=heights[x][y]
           
            if curr_height<par_height:
                return

            visited.add(v)

            dfs((x-1,y),curr_height)
            dfs((x+1,y),curr_height)
            dfs((x,y-1),curr_height)
            dfs((x,y+1),curr_height)

            return
        

        atlantic_neighbors=[]
        pacific_neighbors=[]
        
        for row in range(rows):
            atlantic_neighbors.append((row,cols-1))
            pacific_neighbors.append((row,0))
        
        for col in range(cols):
            atlantic_neighbors.append((rows-1,col))
            pacific_neighbors.append((0,col))

        for pacific_neighbor in pacific_neighbors:
            dfs(pacific_neighbor,-1)
        
        visited_pacific=visited
        visited=set()
        
        for atlantic_neighbor in atlantic_neighbors:
            dfs(atlantic_neighbor,-1)
        visited=visited & visited_pacific


        return list(visited)

                    
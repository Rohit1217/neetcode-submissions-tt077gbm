class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows,cols=len(heights),len(heights[0])
        

        pacific_nodes_l=[(0,idx) for idx in range(cols)]
        pacific_nodes_d=[(idx,0) for idx in range(rows)]

        pacific_node_arr=pacific_nodes_l+pacific_nodes_d
        visited=set()
        
        def dfs(node_with_val):
            r,c,parent_val=node_with_val[0],node_with_val[1],node_with_val[2]

            if r<0 or c<0 or r>rows-1 or c>cols-1 or (r,c) in visited or heights[r][c]<parent_val:
                return
            
            visited.add((r,c))
            neighbors=[(r-1,c,heights[r][c]) ,(r+1,c,heights[r][c]),(r,c-1,heights[r][c]),(r,c+1,heights[r][c]) ]
            
            for neighbor in neighbors:
                dfs(neighbor)
            return
        
        
        for node in pacific_node_arr:
            if node not in visited:
                dfs((node[0],node[1],0))

        
        pacific_set=visited
        visited=set()
        print(visited,pacific_set,"asd")

        atlantic_nodes_l=[(rows-1,idx) for idx in range(cols)]
        atlantic_nodes_d=[(idx,cols-1) for idx in range(rows)]
        atlantic_node_arr=atlantic_nodes_l+atlantic_nodes_d

        
        for node in atlantic_node_arr:
            if node not in visited:
                dfs((node[0],node[1],0))


        both_visited= visited & pacific_set
        
        return list(both_visited)

        
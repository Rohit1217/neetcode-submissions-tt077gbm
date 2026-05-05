class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank=[1]*n
        parent=[i for i in range(n)]

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx,rooty=find(x),find(y)
            if rootx==rooty:
                return False 
            
            if rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            elif rank[rootx]<rank[rooty]:
                parent[rootx]=rooty
            else:
                parent[rooty]=rootx
                rank[rootx]+=1
            return True            

        for edge in edges:
            u,v=edge[0],edge[1]
            if union(u,v)==False:
                return False

        for i in range(n):
            find(i)
        
        if  len(list(set(parent)))>1:
            return False
        return True        
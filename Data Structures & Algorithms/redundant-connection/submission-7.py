class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n=len(edges)
        parent=list(range(n+1))
        rank=[1]*(n+1)
        
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx=find(x)
            rooty=find(y)

            if rank[rootx]<rank[rooty]:
                parent[rootx]=rooty
                
            elif rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            else:
                parent[rooty]=rootx
                rank[rootx]+=1
        
        for edge in edges:
            x,y=edge[0],edge[1]
            if find(x)==find(y):
                return edge
            else:
                union(x,y)
        
        return edge
        




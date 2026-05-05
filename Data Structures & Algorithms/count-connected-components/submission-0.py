class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        rank=[1]*n
        parent=[i for i in range(n)]

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rootx==rooty:
                return 
            
            if rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            elif rank[rootx]<rank[rooty]:
                parent[rootx]=rooty
            else:
                parent[rooty]=rootx
                rank[rootx]+=1
            

        for edge in edges:
            u,v=edge[0],edge[1]
            union(u,v)

        for i in range(n):
            find(i)
        
        return len(list(set(parent)))
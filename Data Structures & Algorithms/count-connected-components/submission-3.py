class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n))
        rank=[0]*(n)


        def find(x):
            if parent[x]==x:
                return x
            else:
                parent[x]=find(parent[x])
            
            return parent[x]
        
        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rank[rootx]==rank[rooty]:
                parent[rooty]=rootx
                rank[rootx]+=1
            elif rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            else:
                parent[rootx]=rooty
            
            return
        

        for edge in edges:
            x,y=edge
            union(x,y)
        
        for i in range(n):
            find(i)
        
        return len(list(set(parent)))
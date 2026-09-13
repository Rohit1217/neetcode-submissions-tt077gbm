class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n))
        rank=[0]*(n)
        components=n  


        def find(x):
            if parent[x]==x:
                return x
            else:
                parent[x]=find(parent[x])
            
            return parent[x]
        
        def union(x,y):
            nonlocal components

            rootx,rooty=find(x),find(y)

            if rootx==rooty:
                return

            if rank[rootx]==rank[rooty]:
                parent[rooty]=rootx
                rank[rootx]+=1
            elif rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            else:
                parent[rootx]=rooty
            components-=1

            return
        

        for edge in edges:
            x,y=edge
            union(x,y)
        
        return components
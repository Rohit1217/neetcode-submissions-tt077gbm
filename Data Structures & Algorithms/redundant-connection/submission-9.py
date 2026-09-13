class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(0,n+1))
        rank=[0]*(n+1)

        def find(x):
            if parent[x]==x:
                return x
            else:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rootx==rooty:
                return False

            if rank[rootx]==rank[rooty]:
                parent[rooty]=rootx
                rank[rootx]+=1
            elif rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            else:
                parent[rootx]=rooty
            return True
        

        for edge in edges:
            x,y=edge
            flag=union(x,y)
            if flag==False:
                return [x,y]





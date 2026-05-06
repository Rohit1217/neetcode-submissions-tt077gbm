class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        rank=[1]*n
        parent=list(range(n))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rootx==rooty:
                return False
            
            if rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            elif rank[rooty]>rank[rootx]:
                parent[rootx]=rooty
            else:
                rank[rootx]+=1
                parent[rootx]=rooty

            return True
        
        for edge in edges:
            u,v=edge
            if union(u,v)==False:
                return False
        
        for i in range(n):
            find(i)
        
        if max(parent)!=min(parent):
            return False

        return True
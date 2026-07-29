class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank=[0 for _ in range(n)]
        parent=[i for i in range(n)]

        if len(edges)!=n-1:
            return False

        def find(x):
            if parent[x]==x:
                return x
            
            parent[x]=find(parent[x])
            return parent[x]
        

        def union(x,y):
            parentx,parenty=find(x),find(y)

            if parentx==parenty:
                return False
            
            if rank[parentx]<rank[parenty]:
                parent[parentx]=parenty
            
            elif rank[parentx]>rank[parenty]:
                parent[parenty]=parentx
            
            elif rank[parentx]==rank[parenty]:
                parent[parentx]=parenty
                rank[parentx]+=1
            
            return True
        

        for src,dest in edges:
            flag=union(src,dest)
            if flag==False:
                return flag
        
        return True

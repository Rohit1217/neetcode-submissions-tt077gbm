class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent={}
        rank={}

        def find(x):
            if x not in parent:
                parent[x]=x
                rank[x]=1

            if x==parent[x]:
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

            if not flag:
                return [x,y]
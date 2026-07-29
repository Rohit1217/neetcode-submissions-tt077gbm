class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        parent={}
        rank={}
        ratio={}

        def find(x):
            if x not in parent:
                parent[x]=x
                rank[x]=0
                ratio[x]=1
                return x

            if parent[x]==x:
                return x

            parent_x=parent[x]
            parent[x]=find(parent[x])

            ratio[x]=ratio[x]*ratio[parent_x]
            return parent[x]


        def union(x,y,val):
            parentx,parenty=find(x),find(y)
            
            if parentx==parenty:
                return
            
            if rank[parentx]==rank[parenty]:
                parent[parenty]=parentx
                rank[parentx]+=1
                ratio[parenty]= ratio[x]/(ratio[y]*val)

            elif rank[parentx]<rank[parenty]:
                parent[parentx]=parenty
                ratio[parentx]= (ratio[y]*val)/ratio[x]

            else:
                parent[parenty]=parentx
                ratio[parenty]= ratio[x]/(ratio[y]*val)
        
        for equation,value in zip(equations,values):
            src,dst=equation
            val=value

            if src not in ratio:
                ratio[src]=1
            if dst not in ratio:
                ratio[dst]=1

            union(src,dst,val)
        
        res=[]
        for query in queries:
            src,dst=query
            if src not in parent or dst not in parent:
                res.append(-1.0)
            elif find(src)==find(dst):
                res.append(ratio[src]/ratio[dst])
            else:
                res.append(-1.0)

        return res




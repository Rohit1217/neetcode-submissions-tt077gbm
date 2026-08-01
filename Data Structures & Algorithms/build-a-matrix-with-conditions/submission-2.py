
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def build_adj_list(conditions):
            indeg_list=[0 for i in range(k+1)]
            adj_list=[[] for i in range(k+1)]
            dependency_order=[0 for i in range(k+1)]

            for condition in conditions:
                src,dst=condition
                adj_list[src].append(dst)
                indeg_list[dst]+=1
            
            return adj_list,indeg_list,dependency_order
        

        def khans(adj,indeg,dependency_order):
            queue=deque([])
            top_order=[]
            
            for u in range(1,k+1):
                if indeg[u]==0:
                    queue.append(u)
            processed=0
            
            while queue:
                u=queue.popleft()
                processed+=1
                top_order.append(u)

                for v in adj[u]:
                    indeg[v]-=1

                    if indeg[v]==0:
                        queue.append(v)
            
            flag=processed==k
            return top_order,flag

        adj_list,indeg_list,dependency_order=build_adj_list(rowConditions)
        rowidx,flag=khans(adj_list,indeg_list,dependency_order)        
        
        if flag==False:
            return []

        adj_list,indeg_list,dependency_order=build_adj_list(colConditions)
        colidx,flag=khans(adj_list,indeg_list,dependency_order)
        
        if flag==False:
            return []

        matrix= [[0 for i in range(k)] for j in range(k)]

        pos_hash={}
        c=0
        for i in rowidx:
            pos_hash[i]=[]
            pos_hash[i].append(c)
            c+=1
        c=0
        for i in colidx:
            pos_hash[i].append(c)
            c+=1

        for i in pos_hash:
            r,c=pos_hash[i]
            matrix[r][c]=i

        return matrix    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        self.timer=0
        self.has_cycle=False
        
        finished=set()
        visited=set()
        self.stack=[]
        adj_list=[[] for _ in range(n)]
        for source,target in edges:
            adj_list[source].append(target)
            adj_list[target].append(source)
        
        print(adj_list)
        
        def dfs(u):
            self.timer+=1
            visited.add(u)
            # if self.has_cycle==True:
            #     return

            for v in adj_list[u]:
                if v not in visited:
                    dfs(v)
                
                # elif v not in finished:
                #     self.has_cycle=True
                #     return
            
            self.timer+=1
            finished.add(u)
            return
        
        for u in range(1):
            if u not in visited:
                dfs(u)
            print(visited)
            if len(list(visited))!=n:
                return False

        return True        

        
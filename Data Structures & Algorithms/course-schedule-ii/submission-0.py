class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.has_cycle=False
        self.timer=0
        self.stack=[]
        discovery_time={}
        finish_time={}
        visited=set()

        adj_list=[[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            adj_list[course].append(pre)
        print(adj_list)        
        def dfs(u):
            self.timer+=1
            discovery_time[u]=self.timer
            visited.add(u)

            
            for v in adj_list[u]:
                if v not in visited:
                    dfs(v)
                elif v not in finish_time.keys():
                    self.has_cycle=True
                    return 
            
            self.timer+=1
            finish_time[u]=self.timer
            self.stack.append(u)

            return 

        for course in range(numCourses):
            if course not in visited:
                dfs(course)
            if self.has_cycle==True:
                return []
        print(self.stack,self.has_cycle)
        return self.stack

            
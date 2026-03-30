class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={}
        visited=set()
        finished=set()
        self.has_cycle=False

        for edge in prerequisites:
            course,prereq=edge[0],edge[1]
            if course not in adj_list:
               adj_list[course]=[prereq]
            else:
                adj_list[course].append(prereq)
        
        def dfs(u):
            visited.add(u)
            if u in adj_list:
                for v in adj_list[u]:
                    if v in visited and  v not in finished:
                        self.has_cycle=True
                        return 
                    if v not in visited:
                        dfs(v)
            finished.add(u)
            return
        
        for course in adj_list.keys():
            if course not in visited:
                flag=dfs(course)
                if self.has_cycle==True:
                    return False

        return True            
        


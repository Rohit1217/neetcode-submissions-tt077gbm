class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        adj_list=[[] for i in range(n)]

        for prereq in prerequisites:
            src,dst=prereq
            adj_list[src].append(dst)
            # print(prereq,src,dst)

        visited=set()
        active=set()
        prereq=[]
        flag=False
        
        def dfs(s):
            nonlocal flag

            if s in visited or flag:
                return
            
            active.add(s)
            
            for d in adj_list[s]:
                if d in active:
                    flag=True
                    return

                dfs(d)

            visited.add(s)
            active.remove(s)
            
            prereq.append(s)
            return
        
        for i in range(n):
            dfs(i)
            if flag:
                return []
        
        return prereq

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for i in range(numCourses)]
        indegree_count=[0 for i in range(numCourses)]

        for crs,preq in  prerequisites:
            adj_list[preq].append(crs)
            indegree_count[crs]+=1

        queue=deque([])
        for crs in range(numCourses):
            if indegree_count[crs]==0:
                queue.append(crs)
        count=0

        while queue:
            curr_crs=queue.popleft()
            count+=1

            for crs in adj_list[curr_crs]:
                indegree_count[crs]-=1

                if indegree_count[crs]==0:
                    queue.append(crs)
            
        if count!=numCourses:
            return False
        
        return True



from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        n=numCourses
        ordered_courses=[]

        adj_list=[[] for i in range(n)]

        indeg_count=[0 for i in range(n)]

        for prereq in prerequisites:
            d,s=prereq
            adj_list[s].append(d)
            indeg_count[d]+=1

        q=deque([])
        for i in range(n):
            if indeg_count[i]==0:
                q.append(i)

        # ordered_set=list(indeg_set)

        num_courses=0

        while q:
            s=q.popleft()
            ordered_courses.append(s)
            num_courses+=1

            for d in adj_list[s]:
                indeg_count[d]-=1
                if indeg_count[d]<0:
                    return []
                if indeg_count[d]==0:
                    q.append(d)
        
        if num_courses!=n:
            return []

        return ordered_courses



        


        
        
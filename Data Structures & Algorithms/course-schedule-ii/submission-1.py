class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list=defaultdict(list)
        courses=list(range(numCourses))

        for prereq in prerequisites:
            course,preq=prereq[0],prereq[1]
            adj_list[preq].append(course)

        colors=defaultdict(int)
        course_order_list=[]
        flag=[False]

        def dfs(node):
            if flag[0]==True:
                return

            colors[node]=1
            
            if node in adj_list:
                for child in adj_list[node]:
                    if colors[child]==1:
                        flag[0]=True
                    elif colors[child]==0:
                        dfs(child)

            colors[node]=2
            course_order_list.append(node)

        for course in courses:
            if flag[0]==True:
                return []
            elif colors[course]==0:
                dfs(course)
        
        return course_order_list[::-1]

                
                    


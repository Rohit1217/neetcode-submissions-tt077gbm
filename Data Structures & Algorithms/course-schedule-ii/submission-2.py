from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses=list(range(numCourses))
        adj_list=defaultdict(list)

        in_deg_arr=[0]*numCourses

        for prereq_list in prerequisites:
            course,prereq=prereq_list[0],prereq_list[1]
            adj_list[prereq].append(course)
            in_deg_arr[course]+=1
        
        queue=deque()
        for course in range(numCourses):
            if in_deg_arr[course]==0:
                queue.append(course)
        
        num_proc=0
        res_list=[]

        while queue:
            curr_course=queue.popleft()
            num_proc+=1
            res_list.append(curr_course)

            for child in adj_list[curr_course]:
                in_deg_arr[child]-=1
                
                if in_deg_arr[child]==0:
                    queue.append(child)
        
        if num_proc!=numCourses:
            return []
        
        return res_list
        
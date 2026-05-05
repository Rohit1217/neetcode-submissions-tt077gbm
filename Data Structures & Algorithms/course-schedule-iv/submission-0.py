from collections import defaultdict,deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n=numCourses
        in_deg_arr=[0]*(n+1)

        adj_list=defaultdict(list)
        prereq_set_arr=[set() for i in range(n+1)]

        for prereq in prerequisites:
            preq,course=prereq[0],prereq[1]
            adj_list[preq].append(course)
            in_deg_arr[course]+=1

        queue=deque()

        for course in range(n):
            if in_deg_arr[course]==0:
                queue.append(course)

        while queue:
            curr_course=queue.popleft()

            for next_course in adj_list[curr_course]:
                prereq_set_arr[next_course].update(prereq_set_arr[curr_course])
                prereq_set_arr[next_course].add(curr_course)

                in_deg_arr[next_course]-=1
                if in_deg_arr[next_course]==0:
                    queue.append(next_course)
        

        res_list=[]
        for query in queries:
            if query[0] in prereq_set_arr[query[1]]:
                res_list.append(True)
            else:
                res_list.append(False)

        return res_list

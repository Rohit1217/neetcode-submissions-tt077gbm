import heapq
from collections import deque,defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_count=defaultdict(int)
        last_seen=defaultdict(int)
        priority_queue=[]
        
        heapq.heapify(priority_queue)
        
        for task in tasks:
            task_count[task]-=1

        for task in task_count:
            heapq.heappush(priority_queue,(task_count[task],task))
        
        curr_time=0
        tasks_completed=0
        
        while tasks_completed!=len(tasks):
            flag=False
            task_update_list=[]

            while not flag and len(priority_queue)>0:
                task_priority,curr_task=heapq.heappop(priority_queue)
                 
                if last_seen[curr_task]==0 or curr_time-last_seen[curr_task]>=n:
                    flag=True
                    task_count[curr_task]+=1
                    last_seen[curr_task]=curr_time+1
                    
                    if task_count[curr_task]!=0:
                        heapq.heappush(priority_queue,(task_priority+1,curr_task))
                    tasks_completed+=1
                
                else:
                    task_update_list.append((task_priority,curr_task))
            
            for task_priority,task in task_update_list:
                heapq.heappush(priority_queue,(task_priority,task))
            
            curr_time+=1
        return curr_time
        
        
        
        
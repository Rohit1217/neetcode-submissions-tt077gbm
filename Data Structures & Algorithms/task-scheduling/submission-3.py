from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        
        count_tasks=Counter(tasks)
        
        tasks_heap=[]

        for task in count_tasks:
            tasks_heap.append((-count_tasks[task],time-n-1,task))
        
        heapq.heapify(tasks_heap)

        invalid_arr=[]
        while tasks_heap or invalid_arr:
            if len(tasks_heap)>0:
                neg_count,last_time,task=heapq.heappop(tasks_heap)
                
                if time-last_time<=n:
                    invalid_arr.append((neg_count,last_time,task))
                else:
                    if neg_count<-1:
                        neg_count+=1
                        last_time=time
                        heapq.heappush(tasks_heap,(neg_count,last_time,task))

                    for elem in invalid_arr:
                        heapq.heappush(tasks_heap,elem)
                    time+=1
                    invalid_arr=[]
            
            else:
                for elem in invalid_arr:
                    heapq.heappush(tasks_heap,elem)
                time+=1
                invalid_arr=[]

        return time




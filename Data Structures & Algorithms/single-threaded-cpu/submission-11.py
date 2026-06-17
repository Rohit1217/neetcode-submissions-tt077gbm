from collections import deque

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time=1
        
        for i in range(len(tasks)):
            tasks[i]=(tasks[i][0],tasks[i][1],i)
        
        tasks.sort()

        proc_order=[]

        tasks_queue=deque(tasks)
        tasks_heap=[]
        heapq.heapify(tasks_heap)

        while tasks_queue or tasks_heap:
            if tasks_heap:
                proc_time,idx=heapq.heappop(tasks_heap)
                time+=proc_time
                proc_order.append(idx)

                while tasks_queue:
                    curr_task=tasks_queue[0]
                    enq_time,proc_time,idx=curr_task

                    if enq_time<=time:
                        heapq.heappush(tasks_heap,(proc_time,idx))
                        tasks_queue.popleft()
                    else:
                        break
            else:
                enq_time,proc_time,idx=tasks_queue.popleft()
                heapq.heappush(tasks_heap,(proc_time,idx))
                time=max(enq_time,time)


        return proc_order


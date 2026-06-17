from collections import Counter,deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        
        count_tasks=Counter(tasks)
        
        tasks_heap=[]
        cooldown_queue=deque()
        for task in count_tasks:
            tasks_heap.append((-count_tasks[task],time-n-1,task))
        
        heapq.heapify(tasks_heap)
        
        while tasks_heap or cooldown_queue:

            if len(tasks_heap)>0:
                neg_count,last_time,task=heapq.heappop(tasks_heap)
                
                if neg_count<-1:
                    neg_count+=1
                    last_time=time
                    cooldown_queue.append((neg_count,last_time,task))
                    

            time+=1

            while cooldown_queue:
                neg_count,last_time,task=cooldown_queue[0]
                if time-last_time>n:
                    heapq.heappush(tasks_heap,(neg_count,last_time,task))
                    cooldown_queue.popleft()
                else:
                    break
            
        return time




import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list=[[] for _ in range(n+1)]

        for edge in times:
            u,v,w=edge
            adj_list[u].append((v,w))
        
        heap=[(0,k)]
        
        heapq.heapify(heap)
        
        processed=[False for i in range(n+1)]
        num_proc=0

        while heap:
            w,u=heapq.heappop(heap)

            if processed[u]!=False:
                continue
            
            processed[u]=True
            num_proc+=1

            if num_proc==n:
                return w

            for edge in adj_list[u]:
                v,ew=edge
                if processed[v]==False:
                    heapq.heappush(heap,(w+ew,v))
        
        return -1
    
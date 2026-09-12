import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list=[[] for i in range(n+1)]
        min_times=[-1]*(n+1)
        min_times[0]=0

        for edge in times:
            u,v,t=edge
            adj_list[u].append((v,t))
        
        heap=[(0,k)]
        min_times[0]=0

        heapq.heapify(heap)

        while heap:
            ct,cu=heapq.heappop(heap)

            if min_times[cu]!=-1:
                continue
            
            min_times[cu]=ct

            for cv,t in adj_list[cu]:
                heapq.heappush(heap,(ct+t,cv))
        
        if -1 in min_times:
            return -1
        return max(min_times)

            


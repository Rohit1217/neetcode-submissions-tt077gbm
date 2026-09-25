import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj_list=[[] for i in range(n+1)]
        
        for time in times:
            u,v,t=time
            adj_list[u].append((v,t))

        heap=[(0,k)]
        heapq.heapify(heap)

        visited=set()
        time=[-1 for i in range(n)]

        while heap:
            t,u=heapq.heappop(heap)

            if u not in visited:
                visited.add(u)
                time[u-1]=t
            else:
                continue

            for v,d in adj_list[u]:
                if v not in visited:
                    heapq.heappush(heap,(t+d,v))
        
        if -1 in time:
            return -1
        return max(time)
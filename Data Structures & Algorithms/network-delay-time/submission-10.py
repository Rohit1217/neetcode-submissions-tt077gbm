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
        time=[float("inf") for i in range(n)]
        time[k-1]=0

        while heap:
            t,u=heapq.heappop(heap)

            if u  in visited:
                continue
            if len(visited)==n:
                break
            
            visited.add(u)
            time[u-1]=t

            for v,d in adj_list[u]:
                if v not in visited and t+d<time[v-1]:
                    heapq.heappush(heap,(t+d,v))
        
        if len(visited)==n:
            return max(time)
        return -1
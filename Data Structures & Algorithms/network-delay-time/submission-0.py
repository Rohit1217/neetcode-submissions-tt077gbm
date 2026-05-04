import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        time_cost_list=[-1]*n
        adj_list=defaultdict(list)
        
        for edge_list in times:
            u,v,t=edge_list[0],edge_list[1],edge_list[2]
            adj_list[u-1].append((v-1,t))
    

        time_heap=[(0,k-1)]
        heapq.heapify(time_heap)

        while time_heap:
            t,u=heapq.heappop(time_heap)
            
            if time_cost_list[u]!=-1:
                continue
            
            time_cost_list[u]=t

            for edge in adj_list[u]:
                v,edge_time=edge[0],edge[1]
                if time_cost_list[v]==-1:
                    heapq.heappush(time_heap,(edge_time+t,v))
        
        if  min(time_cost_list)==-1:
            return -1
        else:
            return max(time_cost_list)
            
            

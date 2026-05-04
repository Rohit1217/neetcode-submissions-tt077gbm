import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        time_cost_list=[-1]*n
        adj_list=defaultdict(list)
        
        for edge_list in times:
            curr_node,next_node,edge_time=edge_list[0],edge_list[1],edge_list[2]
            adj_list[curr_node-1].append((next_node-1,edge_time))
    

        time_heap=[(0,k-1)]
        heapq.heapify(time_heap)

        while time_heap:
            curr_time,curr_node=heapq.heappop(time_heap)
            
            if time_cost_list[curr_node]!=-1:
                continue
            
            time_cost_list[curr_node]=curr_time

            for edge in adj_list[curr_node]:
                next_node,edge_time=edge[0],edge[1]
                if time_cost_list[next_node]==-1:
                    heapq.heappush(time_heap,(edge_time+curr_time,next_node))
        
        if  min(time_cost_list)==-1:
            return -1
        else:
            return max(time_cost_list)
            
            

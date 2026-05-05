import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list=defaultdict(list)
        for flight in flights:
            adj_list[flight[0]].append((flight[1],flight[-1]))

        dist_heap=[(0,0,src)]
        heapq.heapify(dist_heap)
        dist=[-1]*n

        visited=set()
        visited.add(src)

        while dist_heap:
            node_dist,node_steps,node=heapq.heappop(dist_heap)

            dist[node]=node_dist
            visited.add(node)

            if node == dst:
                return node_dist
            
            if node_steps==k+1:
                continue
            
            for (next_node,edge_dist) in adj_list[node]:
                if next_node not in visited:
                    heapq.heappush(dist_heap,(node_dist+edge_dist,node_steps+1,next_node))
        
        
        return dist[dst]




    

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        #BELLMAN FORD
        distances=[float('inf') for _ in range(n)]
        distances[src]=0

        for _ in range(k+1):
            temp_distances=distances.copy()
            for flight in flights:
                fsrc,fdst,fwht=flight
                if distances[fsrc]!=float("inf"):
                    temp_distances[fdst]=min(temp_distances[fdst],distances[fsrc]+fwht)
            
            distances=temp_distances
        
        if distances[dst]==float("inf"):
            return -1
            
        return distances[dst]




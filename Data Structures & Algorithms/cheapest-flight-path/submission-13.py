import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        #bellman ford relax edges slowly k+1 edges

        dst_lengths=[float("inf") for i in range(n)] 
        dst_lengths[src]=0

        for i in range(k+1):
            dst_copy=copy.deepcopy(dst_lengths)
            for flight in flights:
                fsrc,fdst,fcst=flight
                
                if dst_copy[fsrc]!=float("inf"):
                    dst_lengths[fdst]=min(dst_lengths[fdst],dst_copy[fsrc]+fcst)
        

        if dst_lengths[dst]!=float("inf"):
            return dst_lengths[dst]
        return -1



        
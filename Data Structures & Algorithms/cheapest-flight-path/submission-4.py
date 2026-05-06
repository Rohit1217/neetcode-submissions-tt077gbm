class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        inf=1e8
        cost=[inf for i in range(n)]
        cost[src]=0

        for i in range(k+1):
            temp_cost = cost.copy()
            for flight in flights:
                s,d,c=flight[0],flight[1],flight[2]
                
                if temp_cost[s]!=inf:
                    temp_cost[d]=min(temp_cost[d],cost[s]+c)
            
            cost=temp_cost
        
        if cost[dst]==inf:
            return -1
        return cost[dst]


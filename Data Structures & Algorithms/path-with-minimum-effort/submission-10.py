import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols=len(heights),len(heights[0])

        if rows==0 or cols==0:
            return 0
        inf=1e8
        cost=[[inf]*cols for _ in range(rows)]

        cost[0][0]=0

        heap=[(0,0,0)]
        heapq.heapify(heap)
        visited=set()

        while heap:
            curr_node=heapq.heappop(heap)
            price,r,c=curr_node

            if r==rows-1 and c==cols-1:
                return cost[-1][-1]            

            neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for neighbor in neighbors:
                n_r,n_c=neighbor
                if 0<=n_r<rows and 0<=n_c<cols:
                    n_price=max(price,abs(heights[r][c]-heights[n_r][n_c]))

                    if n_price<cost[n_r][n_c]:
                        cost[n_r][n_c]=n_price
                        heapq.heappush(heap,(n_price,n_r,n_c))

        return cost[-1][-1]
            




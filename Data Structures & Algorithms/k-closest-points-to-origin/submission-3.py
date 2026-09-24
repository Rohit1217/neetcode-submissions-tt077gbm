
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist=[(x**2+y**2,x,y) for x,y in points]
        res=[]
        heapq.heapify(dist)

        for i in range(0,k):
            d,x,y=heapq.heappop(dist)
            res.append([x,y])
        
        return res
import heapq,math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calc_dist(x,y):
            return math.sqrt(math.pow(x,2)+math.pow(y,2))

        if len(points)==0:
            return []

        points=[(calc_dist(point[0],point[1]),(point[0],point[1])) for point in points]
        heapq.heapify(points)

        res=[]
        count=0

        while len(points)>0 and count<k:
            res.append(heapq.heappop(points)[1])
            count+=1
        
        return res


        
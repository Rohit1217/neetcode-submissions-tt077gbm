class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        curr_c=0

        car_heap=[]
        heapq.heapify(car_heap)
        
        for trip in trips:
            c,s,e=trip

            #DEBOARD
            while car_heap and car_heap[0][0]<=s:
                curr_c-=car_heap[0][1]
                heapq.heappop(car_heap)

            #BOARD
            if curr_c+c<=capacity:
                heapq.heappush(car_heap,(e,c))
                curr_c+=c
            else:
                return False
        
        
        return True

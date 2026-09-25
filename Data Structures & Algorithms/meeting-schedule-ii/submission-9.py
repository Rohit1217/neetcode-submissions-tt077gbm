"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals=[(i.start,i.end) for  i in intervals]
        intervals.sort()

        rooms=0
        max_rooms=0
        heap=[]

        heapq.heapify(heap)
        
        for interval in intervals:
            s,e=interval
            while heap and heap[0]<=s:
                heapq.heappop(heap)
                rooms-=1
            
            heapq.heappush(heap,e)
            rooms+=1

            max_rooms=max(max_rooms,rooms)
        
        return max_rooms

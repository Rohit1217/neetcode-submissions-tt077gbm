"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        count=0
        intervals.sort(key=lambda l:l.end)
        new_interval=Interval(1e+8,1e+8)
        intervals.append(new_interval)
        start,end=intervals[0].start,intervals[0].end
        for i  in range(1,len(intervals)):
            interval=intervals[i]
            start_i,end_i=interval.start,interval.end
            # print(interval)
            # print(start_i,end_i,start,end)
            if start_i>=end:
                start,end=start_i,end_i
            else:
                return False
        return True


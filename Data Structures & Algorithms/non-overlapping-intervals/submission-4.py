class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda interval : interval[1])
        prev_end=intervals[0][1]

        remove=0
        print(intervals)

        for i in range(1,len(intervals)):
            start,end=intervals[i]

            if start<prev_end:
                remove+=1
            else:
                prev_end=end
        
        return remove
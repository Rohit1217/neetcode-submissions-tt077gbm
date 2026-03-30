class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s_i,f_i=newInterval[0],newInterval[1]
        intervals.append([1002,1003])
        intervals=[[-1,-1]]+intervals
        start=0
        i=0
        while i< len(intervals):
            curr_s,curr_f=intervals[i][0],intervals[i][1]
            next_s,next_f=intervals[i+1][0],intervals[i+1][1]
            if s_i>=curr_s and s_i<next_s:
                start= i
            if f_i>=curr_s and f_i<next_s:
                end=i
                i=len(intervals)
            i+=1
        
        start_s,start_f=intervals[start][0],intervals[start][1]
        end_s,end_f=intervals[end][0],intervals[end][1]

        if s_i>start_f:
            if s_i>end_s:
                requiredInterval=[[start_s,start_f],[s_i,f_i]]
            elif f_i>end_f:
                requiredInterval=[[start_s,start_f],[s_i,f_i]]
            else:
                requiredInterval=[[start_s,start_f],[s_i,end_f]]
        else:
            if f_i>end_f:
                requiredInterval=[[start_s,f_i]]
            else:
                requiredInterval=[[start_s,end_f]]
        print(intervals,start,end,newInterval)
        intervals=intervals[:start]+requiredInterval+intervals[end+1:]

        if [-1,-1 ] in intervals:
            intervals=intervals[1:]
        if [1002,1003] in intervals:
            intervals=intervals[:-1]
        return intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=[]
        intervals.sort(key=lambda l:l[1])
        intervals.append([55555,55555])
        start,end=intervals[0][0],intervals[0][1]
        count=0
        for i in range(len(intervals)):
            start_i,end_i=intervals[i][0],intervals[i][1]
            print(start_i,end_i)
            if start_i>=end:
                count+=1
                res.append([start,end])
                start,end=start_i,end_i
            else:
                continue
                start=min(start,start_i)
                end=max(end,end_i)
        print(res)
        return len(intervals)-1-count        

        
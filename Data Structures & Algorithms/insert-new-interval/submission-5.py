class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        start,end=newInterval[0],newInterval[1]
        for i in range(len(intervals)):
            start_i,end_i=intervals[i][0],intervals[i][1]
            print(start_i,end_i,i)
            if end_i<start:
                res.append([start_i,end_i])
            elif start_i>end:
                res=res+[[start,end]]+intervals[i:]
                return res
            else:
                start=min(start_i,start)
                end=max(end_i,end)
        return res+[[start,end]]


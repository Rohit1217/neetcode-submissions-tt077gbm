class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda l:l[0])
        # print(intervals)
        intervals.append([10002,10003])
        start,end,i=intervals[0][0],intervals[0][1],0
        
        for i in range(len(intervals)):
            start_i,end_i=intervals[i][0],intervals[i][1]
            if end<start_i:
                res.append([start,end])
                start,end=start_i,end_i
            else:
                start=min(start,start_i)
                end=max(end,end_i)
        return res        
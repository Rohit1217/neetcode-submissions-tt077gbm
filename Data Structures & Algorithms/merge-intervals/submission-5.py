class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()


        prev_s=-1
        prev_end=-1

        res=[]

        for interval in intervals:
            start,end=interval

            if start<=prev_end:
                prev_end=max(end,prev_end)
            
            else:
                res.append([prev_s,prev_end])
                prev_s,prev_end=start,end
        
        res.append([prev_s,prev_end])

        return res[1:]
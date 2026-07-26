from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        incoming_edges=defaultdict(int)
        outgoing_edges=defaultdict(int)

        for edge in trust:
            source,sink=edge
            incoming_edges[sink]+=1
            outgoing_edges[source]+=1
        

        for sink in incoming_edges:
            if incoming_edges[sink]==n-1 and outgoing_edges[sink]==0:
                return sink
        
        return -1
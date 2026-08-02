import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r,c=m,n
        dist=[0 for _ in range(c) ]
        dist[0]=1

        for i in range(0,r):
            for j in range(1,c):
                dist[j]=dist[j]+dist[j-1]        
            # print(dist)
        return dist[c-1] 


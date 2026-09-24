
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #monotonice dequqe push pop
        q=deque()

        i=0
        j=0

        res=[]
        n=len(nums)

        while j<n:
            while q and q[-1][0]<nums[j]:
                q.pop()
            
            q.append((nums[j],j))

            if q and q[0][1]<(j-k+1):
                q.popleft()

            if j-i+1==k:
                res.append(q[0][0])
                i+=1

            j+=1
        
        return res
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #dequeu monotonic

        n=len(nums)
        monotonic_queue=deque()

        def push_queue(i,val):

            if monotonic_queue and  monotonic_queue[0][0]<=i-k:
                monotonic_queue.popleft()
            
            while monotonic_queue and monotonic_queue[-1][-1]<val:
                monotonic_queue.pop()
            
            monotonic_queue.append((i,val))
        
        res=[]

        for j in range(k-1):
            push_queue(j,nums[j])
        
        j=k-1

        # print(monotonic_queue,j)

        while j<n:
            push_queue(j,nums[j])
            res.append(monotonic_queue[0][-1])
            j+=1
        
        return res

            





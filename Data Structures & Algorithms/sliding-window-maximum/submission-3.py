import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)

        heap=[]
        heapq.heapify(heap)

        i=0
        j=k-1

        res=[]

        if k>n:
            return heap
        else:
            for m in range(i,j):
                heapq.heappush(heap,(-nums[m],m))
        
        while j<n:

            heapq.heappush(heap,(-nums[j],j))

            flag=True
            val=0
            while flag:
                val,idx=heapq.heappop(heap)
                if idx>i:
                    heapq.heappush(heap,(val,idx))
                    flag=False
                elif idx==i:
                    flag=False

            res.append(-val)
            i+=1
            j+=1

        
        return res

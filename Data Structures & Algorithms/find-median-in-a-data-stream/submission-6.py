import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]  
        self.count=0

        heapq.heapify(self.max_heap)   #Top floor k/2 nums
        heapq.heapify(self.min_heap)  # Bot ceil[k/2] num  

    def addNum(self, num: int) -> None:

        heapq.heappush(self.min_heap,num)
        heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        
        if len(self.max_heap)>len(self.min_heap):
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))

        self.count+=1

    def findMedian(self) -> float:
        # print(self.count,self.min_heap,self.max_heap)
        if self.count%2==1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2
        
        
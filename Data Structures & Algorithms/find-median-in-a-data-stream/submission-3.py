import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]

        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap,-num) #PUSH INTO SMALL
        heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap)) #GET LARGEST OF MIN INTO MAX

        if len(self.max_heap)>len(self.min_heap):
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap)) 
        
        print(self.min_heap,self.max_heap)

    def findMedian(self) -> float:
        if len(self.min_heap)>len(self.max_heap):
            return -self.min_heap[0]
        else:
            return (self.max_heap[0]-self.min_heap[0])/2
        


        
        
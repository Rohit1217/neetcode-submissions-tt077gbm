from collections import defaultdict
import heapq
class FreqStack:
    def __init__(self):
        self.freq_hash=defaultdict(int)
        self.freq_heap=[]
        heapq.heapify(self.freq_heap)
        self.count=0
        

    def push(self, val: int) -> None:
        self.freq_hash[val]+=1
        curr_state=(-self.freq_hash[val],-self.count,val)        
        heapq.heappush(self.freq_heap,curr_state)  

        self.count+=1   

    def pop(self) -> int:
        x,_,val= heapq.heappop(self.freq_heap)
        self.freq_hash[val]-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
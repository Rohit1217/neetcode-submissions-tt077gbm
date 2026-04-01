from collections import deque,defaultdict
class MinStack:

    def __init__(self):
        self.stack=deque()
        self.monotonic_stack=deque()
        self.validity_dict=defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.validity_dict[val]+=1

        if len(self.monotonic_stack)==0 or self.monotonic_stack[-1]>val:
           self.monotonic_stack.append(val)


    def pop(self) -> None:
        val=self.stack[-1]
        if self.stack[-1]==self.monotonic_stack[-1] and self.validity_dict[val]==1:
            self.monotonic_stack.pop()

        out=self.stack.pop()        
        self.validity_dict[val]=max(0,self.validity_dict[val]-1)
        return out

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.monotonic_stack[-1]
        

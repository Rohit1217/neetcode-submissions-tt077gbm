from collections import deque,defaultdict
class MinStack:

    def __init__(self):
        self.stack=deque()
        self.monotonic_stack=deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.monotonic_stack)==0 or self.monotonic_stack[-1]>=val:
           self.monotonic_stack.append(val)


    def pop(self) -> None:
        val=self.stack[-1]
        if self.stack[-1]==self.monotonic_stack[-1]:
            self.monotonic_stack.pop()

        out=self.stack.pop()        
        return out

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.monotonic_stack[-1]
        

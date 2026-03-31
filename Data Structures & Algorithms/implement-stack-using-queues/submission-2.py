from collections import deque
class MyStack:

    def __init__(self):
        self.queue=deque()
        # self.queue2=deque()
        self.n=0
        self.curr_top=0
        # self.flag=True

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.n+=1
        self.curr_top=x     

    def pop(self) -> int:
        if self.n==0:
            return None

        self.n-=1
        for idx in range(self.n-1):
            self.queue.append(self.queue.popleft())
        
        self.curr_top=self.queue.popleft()
        self.queue.append(self.curr_top)
        x=self.queue.popleft()

        return x
        

    def top(self) -> int:
        return self.curr_top
        

    def empty(self) -> bool:
        if self.n==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
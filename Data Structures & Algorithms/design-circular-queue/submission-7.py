class Node:
    def __init__(self,val=-1,next=None):
        self.val=val
        self.next=next
        # # self.is_used=is_used

class MyCircularQueue:

    def __init__(self, k: int):
        self.count=0
        self.start=Node()
        self.k=k

        curr=self.start

        for i in range(self.k-1):
            self.rear=curr
            curr.next=Node()
            curr=curr.next

        self.front=curr
        self.front.next=self.start

        if k==1:
            self.front=Node()
            self.rear=self.front
            self.front.next=self.front



    def enQueue(self, value: int) -> bool:
        if self.count==self.k:
            return False
        
        self.rear=self.rear.next
        self.rear.val=value
        # self.rear.is_used=True
        self.count+=1

        return True

    def deQueue(self) -> bool:
        if self.count==0:
            return False

        # self.front.is_used=False
        self.count-=1
        self.front.val=-1
        self.front=self.front.next
        return True       

    def Front(self) -> int:
        return self.front.val
        

    def Rear(self) -> int:
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.count==0

    def isFull(self) -> bool:
        return self.count==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
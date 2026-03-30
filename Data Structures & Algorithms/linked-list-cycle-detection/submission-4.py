# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False

        slow_pointer=head
        fast_pointer=head
        
        count=0
        
        while fast_pointer.next!=None and fast_pointer.next.next!=None:
            fast_pointer=fast_pointer.next.next
            slow_pointer=slow_pointer.next
            if fast_pointer==slow_pointer:
                return True
            count+=1
            
        count+=2
        
        while count!=0:
            slow_pointer=slow_pointer.next
            if slow_pointer==None:
                return False
            count-=1
        
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        fast=head
        slow=head
        
        mid=None
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        

        mid=slow.next
        slow.next=None
        
        prev=None 

        while mid:
            succ=mid.next
            mid.next=prev
            prev,mid=mid,succ
        
        curr=head

        while prev and curr:
            succ=curr.next
            prev_next=prev.next

            curr.next=prev
            prev.next=succ

            curr,prev=succ,prev_next
            


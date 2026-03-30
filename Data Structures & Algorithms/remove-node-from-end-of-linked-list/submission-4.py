# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        length=0

        while curr:
            length+=1
            curr=curr.next
        
        idx=length-n
        
        if idx<0 or idx>length:
            return head
        
        curr=head
        prev=None
        curr_idx=0
        while curr_idx<idx:
            prev=curr
            curr=curr.next
            curr_idx+=1
        
        if prev==None and curr.next==None:
            return None
        elif prev==None:
            return curr.next

        nxt=curr.next
        prev.next=nxt
        curr.next=None

        return head
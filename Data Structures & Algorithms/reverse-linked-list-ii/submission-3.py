# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,length):
        curr=head
        prev=None
        curr_length=0

        while curr_length<length:
            next=curr.next
            curr.next=prev
            prev,curr=curr,next
            curr_length+=1
        
        return curr,prev,head
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
        proxyhead=ListNode()
        proxyhead.next=head

        curr_left=1
        prev_left=proxyhead

        curr=head

        while curr_left<left:
            prev_left=curr
            curr=curr.next
            curr_left+=1
        
        next_right,right,left=self.reverse(curr,right-left+1)

        left.next=next_right
        prev_left.next=right

        return proxyhead.next


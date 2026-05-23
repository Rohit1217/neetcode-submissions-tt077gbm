# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #chalande raja bhramande wadu

        if head is None or head.next is None:
            return 
        
        n=0
        tmp_head=head

        while tmp_head:
            tmp_head=tmp_head.next
            n+=1

        mid=head
        prev=None
        for i in range(n//2):
            prev=mid
            mid=mid.next

        prev.next=None
        mid_mid=mid

        while mid:
            right=mid.next
            mid.next=prev
            prev=mid
            mid=right

        curr=head
        
        while curr:
            next_h=curr.next
            next_prev=prev.next

            curr.next=prev
            prev.next=next_h

            prev_prev=prev
            prev,curr=next_prev,next_h
            

        if (n%2)==1:
            prev_prev.next=mid_mid
            mid_mid.next=None

                                    

        
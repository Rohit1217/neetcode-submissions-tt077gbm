# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n=0

        tmp_head=head

        while tmp_head:
            tmp_head=tmp_head.next
            n+=1

        curr=head
        

        for i in range(n//2):
            next_n=curr.next
            
            while next_n.next:
               prev=next_n
               next_n=next_n.next


            curr_next=curr.next
            curr.next,next_n.next=next_n,curr_next
            prev.next=None

            curr=curr_next

        return        
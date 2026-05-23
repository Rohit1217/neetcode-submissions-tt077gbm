# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        head_fast=head.next.next
        head_slow=head.next

        while head_fast:
            if head_fast.val==head_slow.val:
                return True
            elif head_fast.next:
                head_fast=head_fast.next.next
                head_slow=head_slow.next
            else:
                return False
        
        return False
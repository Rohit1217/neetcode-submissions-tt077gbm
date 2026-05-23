# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        proxyHead=ListNode(0,head)

        curr=proxyHead
        prev=None

        length=0
        while curr:
            curr=curr.next
            length+=1

        curr=proxyHead
        n=length-n

        for i in range(n):
            prev=curr
            curr=curr.next
    
        if curr is None:
            return head
        
        print(n,curr.val)
        succ=curr.next
        prev.next=succ

        return proxyHead.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return 
        length=0
        curr=head

        while curr!=None:
            length+=1
            curr=curr.next
        
        curr=head
        count=0
        while count<length//2:
            count+=1
            curr=curr.next

        #rev list
        if curr.next!=None:
            prev=curr
            curr=curr.next    
            prev.next=None

        while curr!=None:
            next=curr.next    
            curr.next=prev
            prev=curr
            curr=next
        
        curr2=prev
        curr1=head

        while curr2.next!=None :
            next1=curr1.next
            next2=curr2.next
            curr1.next=curr2
            curr2.next=next1
            curr2=next2
            curr1=next1





        return None
        
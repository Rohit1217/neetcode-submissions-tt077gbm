# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        proxyhead=ListNode(0,head)

        curr=proxyhead.next
        count=1
        prev=proxyhead


        while curr:
            if count==left:
                curr2=curr
                prev2=None

                while count<=right:
                    temp=curr2.next
                    curr2.next=prev2
                    prev2=curr2
                    curr2=temp
                    count+=1

                curr.next=curr2
                prev.next=prev2
                
                return proxyhead.next    

            prev=curr    
            curr=curr.next
            count+=1
        
        return proxyhead.next
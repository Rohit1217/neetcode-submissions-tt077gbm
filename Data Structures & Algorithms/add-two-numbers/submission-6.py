# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import string
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        exp=1
        num1=0
        num2=0
        while l1!=None:
            carry=carry+l1.val
            num1+=exp*(carry%10)
            carry=carry//10
            exp=exp*10
            l1=l1.next
        
        num1+=carry*exp    
        carry=0
        exp=1

        while l2!=None:
            carry=carry+l2.val
            num2+=exp*(carry%10)
            carry=carry//10
            exp=exp*10
            l2=l2.next
        
        num2+=carry*exp 

        new_head=ListNode()
        sums=num1+num2
        print(sums)
        x=int(str(sums)[::-1])
        curr=new_head
        print(sums,num1,num2,x)
        while sums!=0:
            curr_num=sums%10
            sums=sums//10
            curr.next=ListNode(curr_num)
            curr=curr.next

        if new_head.next!=None:
            new_head=new_head.next

        return new_head 
        

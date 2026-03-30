# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeTwoListsRec( list1: Optional[ListNode], list2: Optional[ListNode],res:Optional[ListNode]) -> Optional[ListNode]:
            if list1==None:
                res.next=list2
            elif list2==None:
                res.next=list1
            else:
                if list1.val<list2.val:
                    res.next=list1
                    list1=list1.next
                    res=res.next
                    mergeTwoListsRec(list1,list2,res)
                else:
                    res.next=list2
                    list2=list2.next
                    res=res.next
                    mergeTwoListsRec(list1,list2,res)
        
        res=ListNode()
        mergeTwoListsRec(list1,list2,res)
        res=res.next
        return res








        
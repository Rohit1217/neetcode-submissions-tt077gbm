"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr=head

        proxyHead=Node(0)
        new_curr=proxyHead
        nodeList=[]
        idx=0
        
        while curr:
            newHead=Node(curr.val,curr.next,curr)
                        
            new_curr.next=newHead
            new_curr=newHead
            curr.val=idx
            curr=curr.next

            nodeList.append(newHead)
            idx+=1
        
        curr=head
        newHead=proxyHead.next

        while curr:
            random_pointer=curr.random
            if random_pointer:
                newHead.random=nodeList[curr.random.val]
            else:    
                newHead.random=None
            

            curr=curr.next
            newHead=newHead.next

        return proxyHead.next

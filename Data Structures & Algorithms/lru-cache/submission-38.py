from collections import defaultdict

class Node:
    def __init__(self,val=None,key=None,next=None,prev=None):
        self.val=val
        self.key=key
        self.next=next
        self.prev=prev


class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.count=0

        self.proxyhead=Node()
        self.proxytail=Node()
        self.proxytail.next,self.proxyhead.prev=self.proxyhead,self.proxytail

        self.loc_map={}

    def get(self, key: int) -> int:        
        if key not in self.loc_map:
            return -1

        tail=self.proxytail.next

        node=self.loc_map[key]

        if tail.key==node.key:
            return node.val
        
        node.prev.next=node.next
        node.next.prev=node.prev

        tail.prev=node
        node.prev=self.proxytail
        node.next=tail
        self.proxytail.next=node

        self.loc_map[key]=node
        return self.loc_map[key].val
        
    def put(self, key: int,value: int) -> None:
        tail,head=self.proxytail.next,self.proxyhead.prev

        if key in self.loc_map:
            node=self.loc_map[key]
            node.val=value

            if tail.key==node.key:
                return 

            node.prev.next=node.next
            node.next.prev=node.prev
        
        elif self.count==self.cap:
            node=Node(value,key)

            head.prev.next=self.proxyhead
            self.proxyhead.prev=head.prev
            del self.loc_map[head.key]
            tail = self.proxytail.next 

        else:
            self.count+=1
            node=Node(value,key)

        tail.prev=node
        node.prev=self.proxytail
        node.next=tail
        self.proxytail.next=node

        self.loc_map[key]=node
        
        



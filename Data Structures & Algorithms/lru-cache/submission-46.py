class Node:
    def __init__(self,val=0,key=0,nex=None,prev=None):
        self.val=val
        self.nex=nex
        self.prev=prev
        self.key=key

class LRUCache:

    def __init__(self, capacity: int):
        self.proxy_h=Node(0)
        self.proxy_t=Node()

        self.proxy_h.prev,self.proxy_t.nex=self.proxy_t,self.proxy_h
        
        self.key_hash={}
        self.capacity=capacity
        self.count=0
    
    def update(self,node):
        #Delete key ammend its prev nex

        prev,nex=node.prev,node.nex
        prev.nex,nex.prev=nex,prev
        
        #Append key just before proxy_H
        node.nex,node.prev=self.proxy_h,self.proxy_h.prev
        self.proxy_h.prev.nex,self.proxy_h.prev=node,node
        return
    
    def get(self, key: int) -> int:
        if key in self.key_hash:
            node=self.key_hash[key]
            self.update(node)
            return node.val
        #LRU self.update
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_hash:
            node=self.key_hash[key]
            node.val=value
            self.update(node)
        else:
            node=Node(value,key)
            self.key_hash[key]=node
            
            node.nex,node.prev=self.proxy_h,self.proxy_h.prev
            self.proxy_h.prev.nex,self.proxy_h.prev=node,node

            if self.capacity==self.count:
                tail=self.proxy_t.nex
                self.proxy_t.nex,tail.nex.prev=tail.nex,self.proxy_t
                del self.key_hash[tail.key]
            else:
                self.count+=1

        

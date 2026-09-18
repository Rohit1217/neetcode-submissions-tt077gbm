class Node:
    def __init__(self,val=0,key=0):
        self.val=val
        self.key=key
        self.nex=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.size=0
        self.capacity=capacity

        self.proxy_head=Node()
        self.proxy_tail=Node()

        self.proxy_head.prev=self.proxy_tail
        self.proxy_tail.nex=self.proxy_head

        self.key_hash={}

    def get(self, key: int) -> int:
        if key in self.key_hash:
            node=self.key_hash[key]
            prev,nex=node.prev,node.nex
            
            node.nex.prev,node.prev.nex=node.prev,node.nex #Delete middle node connect its prev next
            lu_node=self.proxy_head.prev #prev used nodde
            
            lu_node.nex,self.proxy_head.prev=node,node  #connect prev lu and prox head to lru
            node.prev,node.nex=lu_node,self.proxy_head #connect node to prev lu and prox head

            return self.key_hash[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        #key already present
            if key in self.key_hash:
                node=self.key_hash[key]
                prev,nex=node.prev,node.nex

                node.nex.prev,node.prev.nex=node.prev,node.nex #Delete middle node connect its prev next

                lu_node=self.proxy_head.prev #prev used nodde
                lu_node.nex,self.proxy_head.prev=node,node  #connect prev lu and prox head to lru
                node.prev,node.nex=lu_node,self.proxy_head #connect node to prev lu and prox head
                node.val=value
        
            else:
                node=Node(value,key)
                lu_node=self.proxy_head.prev #prev used nodde
                lu_node.nex,self.proxy_head.prev=node,node  #connect prev lu and prox head to lru
                node.prev,node.nex=lu_node,self.proxy_head #connect node to prev lu and prox head

                self.key_hash[key]=node
                self.size+=1
            
            if self.size>self.capacity:
                lu_node=self.proxy_tail.nex #prev used nodde
                nex_lu_node=lu_node.nex
                self.proxy_tail.nex,nex_lu_node.prev=nex_lu_node,self.proxy_tail
                
                key=lu_node.key
                del self.key_hash[key]

                self.size-=1
            
            
                

            


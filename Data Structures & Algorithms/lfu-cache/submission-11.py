class Node:
    def __init__(self,key=None,val=None,count=0,next=None,prev=None):
        self.val=val
        self.key=key
        self.count=count
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.tail.prev=self.head
        self.head.next=self.tail  
        self.length=0    
    
    def add_node(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self.length+=1
        return

    def del_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.length-=1
        return

    def update_val(node,value):
        node.val=value
        return

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.total_length=0

        self.linked_list_hash={}
        self.min_count=1
        self.key_hash={}

    def init_add_linked_list(self,count,node):
        if count not in self.linked_list_hash:
            linked_list=LinkedList()
            linked_list.add_node(node)
            self.linked_list_hash[count]=linked_list

            # min count can only decrement if new linked list of lower count created
            if count<self.min_count:
                self.min_count=count 
        else:
            linked_list=self.linked_list_hash[count]
            linked_list.add_node(node)
        node.count+=1
        return

    def check_del_linked_list(self,count):
        if self.linked_list_hash[count].length==0:
            del self.linked_list_hash[count]
            if count==self.min_count: 
                self.min_count+=1
        
        #If deletion means one entry list where entry increment by one so min_count increased by one

        return
    def print_all_ll(self):
        for key in self.linked_list_hash:
            ll=self.linked_list_hash[key]
            curr=ll.head.next

            while curr!=ll.tail:
                print(curr.val,key,"PRINT")
                curr=curr.next
    
    def get(self, key: int) -> int:
        if key in self.key_hash:
            node=self.key_hash[key]
            count=node.count
            
            self.linked_list_hash[count].del_node(node)
            self.init_add_linked_list(count+1,node)
            self.check_del_linked_list(count)
            print(count,key,"GET",self.linked_list_hash,self.min_count)
            self.print_all_ll()
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_hash:
            node=self.key_hash[key]
            count=node.count
            node.val=value

            self.linked_list_hash[count].del_node(node)
            
            self.init_add_linked_list(count+1,node)
            self.check_del_linked_list(count)
            self.print_all_ll()

        else:
            count=1
            node=Node(key,value)
            print(node.key,node.val,"NODE")
            self.key_hash[key]=node

            if self.total_length<self.capacity:
                self.init_add_linked_list(count,node)
                self.total_length+=1
                
            else:
                
                linked_list=self.linked_list_hash[self.min_count]
                del self.key_hash[linked_list.tail.prev.key]
                linked_list.del_node(linked_list.tail.prev)
                

                self.check_del_linked_list(self.min_count)
                self.init_add_linked_list(count,node)

        print("PUT",self.linked_list_hash,key,value,self.total_length,self.capacity,self.min_count)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
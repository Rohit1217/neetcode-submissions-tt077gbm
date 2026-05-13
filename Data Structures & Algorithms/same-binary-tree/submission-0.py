# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag=True

        def is_same_rec(node_p,node_q):
            if node_p is None and node_q is not None:
                self.flag=False
                return 
            elif node_p is not None and node_q is  None:
                self.flag=False
                return 
            elif node_p is None and node_q is None:
                return

            elif node_p.val!=node_q.val:
                self.flag=False
                return
            
            elif self.flag==False:
                return
             
            else:
                is_same_rec(node_p.left,node_q.left)
                is_same_rec(node_p.right,node_q.right)
            
            return
        
        is_same_rec(p,q)
        return self.flag
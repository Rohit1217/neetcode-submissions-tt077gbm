# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        proxyroot=TreeNode(float("inf"))
        proxyroot.left=root
        
        # stack=[proxyroot]
        dirs=None
        
        curr=proxyroot
        parent=proxyroot
        while curr and curr.val!=key:
            if curr.val>key:
                parent=curr
                curr=curr.left
                dirs="left"
            elif curr.val<key:
                parent=curr
                curr=curr.right
                dirs="right"

        node=curr                
        if node is None:
            return proxyroot.left

        if node.left is None and node.right is None:
            if dirs=="left":
                parent.left=None
            else:
                parent.right=None
        
        elif node.left is None:
            if dirs=="left":
                parent.left=node.right
            else:
                parent.right=node.right

        elif node.right is None:
            if dirs=="left":
                parent.left=node.left
            else:
                parent.right=node.left

        else:
            succ_p=node
            succ=node.left
            dirs="left"
            
            while succ.right!=None:
                succ_p=succ
                succ=succ.right
                dirs="right"

            node.val=succ.val
            if dirs=="left":
                succ_p.left=succ.left
            else:
                succ_p.right=succ.left

        return proxyroot.left


        
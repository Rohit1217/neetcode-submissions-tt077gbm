# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        proxyroot=TreeNode(key-1)
        proxyroot.left=root
        
        stack=[proxyroot]
        node=None
        dirs=None
        
        while stack:
            parent=stack.pop()
            if parent:
                if  parent.left and parent.left.val==key:
                    node=parent.left
                    dirs="left"
                    break
                if  parent.right and parent.right.val==key:
                    node=parent.right
                    dirs="right"
                    break
                
                stack.append(parent.left)
                stack.append(parent.right)
        
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
                succ_p.left=None
            else:
                succ_p.right=None

        return proxyroot.left


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pos=1
        og_root=root
        prev_node=root

        while root is not None:
            prev_node=root
            if root.val>val:
                root=root.left
                pos=1
            else:
                root=root.right
                pos=-1
        
        new_node=TreeNode(val)

        if prev_node is None:
            return new_node

        if pos==-1:
            prev_node.right=new_node
        else:
            prev_node.left=new_node

        return og_root
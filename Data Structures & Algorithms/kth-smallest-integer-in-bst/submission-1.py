# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_trav(root):
            if root is None:
                return []
            else:
                return inorder_trav(root.left) + [root.val] + inorder_trav(root.right)
        

        sorted_tree=inorder_trav(root)

        return sorted_tree[k-1]
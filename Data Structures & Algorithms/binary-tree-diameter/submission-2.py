# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDim=0
        
        def max_dim_rec(node):
            if node is None:
                return 0
            else:
                right_dim,left_dim= max_dim_rec(node.left), max_dim_rec(node.right)           
                self.maxDim=max(self.maxDim,right_dim+left_dim)
                return max(right_dim+1,left_dim+1)

        max_dim_rec(root)
        return self.maxDim
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.flag=True
        
        def check_height(node):
            if node is None:
                return 0
            else:
                left_height=check_height(node.left)
                right_height=check_height(node.right)
                
                if abs(right_height-left_height)>1:
                    self.flag=False
                
                return 1+max(left_height,right_height)

        check_height(root)
        return self.flag
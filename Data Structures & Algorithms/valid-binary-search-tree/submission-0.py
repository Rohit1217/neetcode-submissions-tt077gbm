# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid_rec(root):
            flag=False

            if root is None:
                return float("inf"),float("-inf"),True

            left_min,left_max,left_flag=isvalid_rec(root.left)
            right_min,right_max,right_flag=isvalid_rec(root.right)
            
            if left_flag and right_flag:
                if left_max<root.val and right_min>root.val:
                    flag=True

            return min(left_min,right_min,root.val),max(left_max,right_max,root.val),flag
        
        _,_,flag=isvalid_rec(root)
        return flag
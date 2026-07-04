# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res=None
        count=0
        
        def kth_smallest(root):
            nonlocal res,count

            if root is None or res is not None:
                return

            kth_smallest(root.left)
            count+=1

            if count==k:
                res=root.val
                return
            
            kth_smallest(root.right)

        
        kth_smallest(root)
        return res
            
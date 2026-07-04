# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count=0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res=None
        def kth_smallest(root):
            nonlocal res

            if root is None or res is not None:
                return

            kth_smallest(root.left)
            self.count+=1

            if self.count==k:
                res=root.val
                return
            
            kth_smallest(root.right)

        
        kth_smallest(root)
        return res
            
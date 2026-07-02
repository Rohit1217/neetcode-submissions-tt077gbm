# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr=root

        if curr is None:
            return None

        if key<curr.val:
            curr.left=self.deleteNode(curr.left,key)

        elif key>curr.val:
            curr.right=self.deleteNode(curr.right,key)
        
        else:
            if curr.right is None:
                return curr.left
            elif curr.left is None:
                return curr.right

            succ=curr.right

            while succ.left:
                succ=succ.left
            
            curr.val=succ.val

            curr.right=self.deleteNode(curr.right,succ.val)


        return curr
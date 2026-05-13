# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res=[]
        processed=set()

        if root is not None:
            stack.append(root)


        while stack:
            curr_node=stack[-1]
            
            if curr_node in processed:
                stack.pop()
                res.append(curr_node.val)
            
            else:
                stack.pop()
                if curr_node.right  is not None:
                    stack.append(curr_node.right)
                
                stack.append(curr_node)

                if curr_node.left  is not None:
                    stack.append(curr_node.left)

                processed.add(curr_node)
    
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        queue=deque([(root,0)])
        prev_level=-1

        level_order=[]

        while queue:
            curr_node,level=queue.popleft()
            
            if curr_node:
                if prev_level==level:
                    level_order[-1].append(curr_node.val)
                else:
                    prev_level=level
                    level_order.append([curr_node.val])

                queue.append((curr_node.left,level+1))
                queue.append((curr_node.right,level+1))
        
        return level_order

        
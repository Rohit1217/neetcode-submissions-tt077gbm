# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent_dict={}
        hq=0
        hp=0

        def parent_traversal(node,parent,height):
            nonlocal hp
            nonlocal hq

            if node is None:
                return
            else:
                if node.val==p.val:
                    hp=height+1
                if node.val==q.val:
                    hq=height+1

                parent_dict[node.val]=(parent,height)
                parent_traversal(node.left,node,height+1)
                parent_traversal(node.right,node,height+1)
                return

        parent_traversal(root,None,0)
        print(parent_dict)
        curr_parent_p=p
        curr_parent_q=q

        while curr_parent_p is not None and curr_parent_q is not None:
            print(curr_parent_p.val,curr_parent_q.val,hp,hq)
            if curr_parent_p.val==curr_parent_q.val:
                return curr_parent_p
            elif hq>hp:
                curr_parent_q,hq=parent_dict[curr_parent_q.val]
            else:
                print(curr_parent_p.val,hp,"saf")
                curr_parent_p,hp = parent_dict[curr_parent_p.val]
        return root

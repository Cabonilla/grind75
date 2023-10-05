# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root, lvl):
            if not root:
                return []

            if len(res) == lvl:
                res.append(root.val)
            preorder(root.right, lvl + 1)
            preorder(root.left, lvl + 1)
            return

        preorder(root, 0)
        return res
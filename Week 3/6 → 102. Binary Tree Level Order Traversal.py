# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bnk = collections.defaultdict(list)

        def walk(root, lvl=0):
            if not root:
                return

            bnk[lvl].append(root.val)
            walk(root.left, lvl+1)
            walk(root.right, lvl+1)

        walk(root)
        return bnk.values()
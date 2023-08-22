# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            lft = dfs(root.left)
            rgt = dfs(root.right)
            diameter = max(diameter, lft + rgt)
            return max(lft, rgt) + 1

        dfs(root)
        return diameter
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        def dfs(root):
            if not root:
                return 0

            lft = dfs(root.left)
            rgt = dfs(root.right)

            if abs(lft - rgt) > 1:
                self.bal = False

            return max(lft, rgt) + 1

        dfs(root)
        return self.bal
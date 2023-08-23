# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bnk = []

        def inorder(root):
            if root is None:
                return None

            inorder(root.left)
            bnk.append(root.val)
            inorder(root.right)
            
        inorder(root)
        if bnk == list(sorted(set(bnk))):
            return True

        return False
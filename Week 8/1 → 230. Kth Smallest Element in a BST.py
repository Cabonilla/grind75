# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Standard In Order.
        ret = []
        def dfs(node):
            if not node:
                return 0

            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)

        dfs(root)
        print(ret)
        return ret[k - 1]
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        def dfs(node):
            if not node:
                return 0

            dfs(node.left)
            if len(ret) == k:
                return
            ret.append(node.val)
            dfs(node.right)

        dfs(root)
        print(ret)
        return ret[-1]
            
            
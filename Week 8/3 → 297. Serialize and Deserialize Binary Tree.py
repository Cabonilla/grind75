# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def serialize(self, root: 'TreeNode') -> str:
    """Encodes a tree to a single string."""
    bnk = []

    def preDFS(root):
      if not root:
        bnk.append('*')
        return

      bnk.append(str(root.val))
      preDFS(root.left)
      preDFS(root.right)

    preDFS(root)
    return ' '.join(bnk)

  def deserialize(self, data: str) -> 'TreeNode':
    """Decodes your encoded data to tree."""
    pop = collections.deque(data.split())

    def revPreDFS():
      node = pop.popleft()
      if node == '*':
        return None

      root = TreeNode(node)
      root.left = revPreDFS()
      root.right = revPreDFS()
      return root

    return revPreDFS()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
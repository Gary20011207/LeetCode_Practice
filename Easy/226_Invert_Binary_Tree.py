# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None
        # Recursive Approach (DFS)
        left_side = self.invertTree(root.left)
        right_side = self.invertTree(root.right)
        # Swap and reconnect child nodes
        root.left, root.right = right_side, left_side

        return root
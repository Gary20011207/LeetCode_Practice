# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case (depth = 0)
        if not root:
            return 0
        # Recursive Approach (DFS)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # Return the maximum depth + current node
        return max(left_depth, right_depth) + 1
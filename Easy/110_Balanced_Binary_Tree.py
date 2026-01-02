# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Returns the height of the tree if balanced, else returns -1 (Depth First Search)
        def getHeight(root):
            # Base case
            if not root:
                return 0
            # Get heights and check if subtrees are already unbalanced
            left_height = getHeight(root.left)
            if left_height == -1:
                return -1
            # Get heights and check if subtrees are already unbalanced
            right_height = getHeight(root.right)
            if right_height == -1:
                return -1
            # Check if current node violates the balance condition
            if abs(left_height - right_height) > 1:
                return -1
            # Return height
            return max(left_height, right_height) + 1
        # Tree is balanced if root doesn't return -1
        return getHeight(root) != -1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Returns (height, max_diameter) for the given subtree (Depth First Search)
        def dfs(root):
            # Base case
            if not root:
                return 0, 0
            left_height, left_diameter = dfs(root.left)
            right_height, right_diameter = dfs(root.right)
            # Height calculation
            curr_height = max(left_height, right_height) + 1
            # Diameter calculation (Check if max path is through current node or within subtrees)
            curr_diameter = max(left_height + right_height, left_diameter, right_diameter)

            return curr_height, curr_diameter
        
        _, max_diameter = dfs(root)
        
        return max_diameter
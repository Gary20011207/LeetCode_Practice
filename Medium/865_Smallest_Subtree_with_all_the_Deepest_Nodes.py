# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # Base case (Reach a null node, return depth 0 and no candidate)
            if not node:
                return (0, None)
            # Get depth and candidate from children (Post-order Traversal)
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            # Deepest nodes are only in the left subtree
            if left_depth > right_depth:
                return (left_depth + 1, left_node)
            # Deepest nodes are only in the right subtree
            elif right_depth > left_depth:
                return (right_depth + 1, right_node)
            # Both sides have same depth; current node is the LCA
            else:
                return (left_depth + 1, node)
        # Return only the candidate node from the result pair
        return dfs(root)[1]
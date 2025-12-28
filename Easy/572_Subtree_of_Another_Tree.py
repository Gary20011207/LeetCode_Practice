# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function (LeetCode #100 Same Tree)
        def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if (not root1) and (not root2):
                return True
            if ((not root1) or (not root2)) or (root1.val != root2.val):
                return False
            
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        # Base case (If main tree is empty, subRoot cannot be found)
        if not root:
            return False
        # Match at current node OR search in left / right children
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
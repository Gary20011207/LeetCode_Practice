# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack for backtracking parent nodes
        stack = []
        curr = root
        # Iterative Inorder Traversal (Left -> Root -> Right)
        while (stack) or (curr):
            # Push all left children to stack
            while curr:
                stack.append(curr)
                curr = curr.left
            # Pop from stack (Smallest available node)
            curr = stack.pop()
            k -= 1
            # Check if k-th smallest is reached
            if k == 0:
                return curr.val
            # Move to the right subtree
            curr = curr.right
        # Fallback
        return -1
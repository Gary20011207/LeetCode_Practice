from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        res_level, curr_level = 1, 1
        queue = deque([root])
        # Breadth First Search (BFS) Appraoch
        while queue:
            level_size = len(queue)
            level_sum = 0
            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                # Add child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Update global maximum and its corresponding level
            if level_sum > max_sum:
                max_sum = level_sum
                res_level = curr_level
            curr_level += 1

        return res_level
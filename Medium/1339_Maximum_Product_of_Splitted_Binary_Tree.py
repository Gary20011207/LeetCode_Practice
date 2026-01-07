# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        # List to store the sum of every subtree
        all_subtree_sums = []
        # Depth First Search Approach to computes sums and stores them
        def dfs(node):
            # Base case
            if not node:
                return 0
            # Calculate current subtree sum using post-order traversal
            curr_sum = node.val + dfs(node.left) + dfs(node.right)
            # Record the sum of this subtree
            all_subtree_sums.append(curr_sum)

            return curr_sum
        # Get total sum first
        total_sum = dfs(root)
        # Find max product
        max_product = 0
        for s in all_subtree_sums:
            # product = (subtree_sum) * (remaining_subtree_sum)
            max_product = max(max_product, s * (total_sum - s))

        return max_product % MOD
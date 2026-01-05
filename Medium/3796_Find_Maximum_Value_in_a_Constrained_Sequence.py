class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        # Initialize limits with infinity, set a[0] to 0
        limit = [float("inf")] * n
        limit[0] = 0
        # Apply fixed constraints from restrictions
        for idx, maxVal in restrictions:
            limit[idx] = maxVal
        # Forward pass (Propagate constraints from left to right)
        for i in range(n - 1):
            limit[i + 1] = min(limit[i + 1], limit[i] + diff[i])
        # Backward pass (Propagate constraints from right to left)
        for i in reversed(range(1, n)):
            limit[i - 1] = min(limit[i - 1], limit[i] + diff[i - 1])
        # The largest value in the sequence will be the maximum of these tightest bounds
        return max(limit)
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # Negative signs can move to any position
        # Total negatives can only be reduced in pairs; odd/even is invariant
        # If odd negatives, leave the one with the smallest abs value
        is_negative_odd = False
        total_sum, min_num = 0, float('inf')
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                # Track parity of negative numbers
                if val < 0:
                    is_negative_odd = not is_negative_odd
                # Keep track of the smallest absolute value
                min_num = min(min_num, abs(val))
                # Assume all numbers can be made positive
                total_sum += abs(val)
        # If negatives are odd, one element must stay negative (Pick the smallest)
        return total_sum - 2 * min_num if is_negative_odd else total_sum
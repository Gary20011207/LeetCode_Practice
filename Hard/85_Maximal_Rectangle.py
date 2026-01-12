class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        c = len(matrix[0])
        # heights[i]: Consecutive 1s above current row
        # Add a 0 at the end as a sentinel to pop all remaining bars
        heights = [0] * (c + 1)
        max_area = 0
        for row in matrix:
            # Update histogram heights for the current row
            for i in range(c):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            # Use a monotonic increasing stack to find max area in histogram
            # Stack stores indices of bars in non-decreasing height order
            # -1 Acts as a sentinel value for the left boundary
            stack = [-1]
            for i in range(c + 1):
                # If current bar is shorter, pop and calculate area for the popped bar
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    # Width is determined by the distance between new stack top and current index
                    w = (i - stack[-1]) - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
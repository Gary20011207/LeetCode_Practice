class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # Store flags for first row / col
        row0_has_zero = any(matrix[0][j] == 0 for j in range(n))
        col0_has_zero = any(matrix[i][0] == 0 for i in range(m))
        # Mark zeros on first row / col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Use markers to fill zeros
        for i in range(1, m):
            for j in range(1, n):
                if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                    matrix[i][j] = 0
        # Handle first row / col flags
        if row0_has_zero:
            matrix[0] = [0] * n
        if col0_has_zero:
            for i in range(m):
                matrix[i][0] = 0
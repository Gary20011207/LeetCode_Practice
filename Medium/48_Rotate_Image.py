class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for i in range(0, len(matrix)):
            # j from i + 1 ensures we only swap the upper triangle
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse (Reflect each row horizontally)
        n = len(matrix[0])
        for row in matrix:
            for i in range(0, n // 2):
                row[i], row[(n - 1) - i] = row[(n - 1) - i], row[i]
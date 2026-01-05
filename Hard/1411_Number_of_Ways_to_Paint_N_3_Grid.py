class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Standard matrix multiplication for 2x2 matrices under modulo
        def multiply(A, B):
            C = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD

            return C
        # Binary Rxponentiation (Fast Exponentiation) Algorithm for matrices
        def matrix_pow(A, p):
            # Identity Matrix
            res = [[1, 0], [0, 1]]
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, A)
                A = multiply(A, A)
                p //= 2

            return res
        
        # Base case
        if n == 1:
            # ABA (3 * 2) + ABC (3 * 2 * 1) = 12
            return 12
        # Transitions (ABA -> 3 ABA, 2 ABC | ABC -> 2 ABA, 2 ABC)
        T = [[3, 2], [2, 2]]
        T_n_minus_1 = matrix_pow(T, n - 1)
        # Calculate final counts by multiplying T^(n - 1) with initial [6, 6] vector
        final_aba = (T_n_minus_1[0][0] * 6 + T_n_minus_1[0][1] * 6) % MOD
        final_abc = (T_n_minus_1[1][0] * 6 + T_n_minus_1[1][1] * 6) % MOD

        return (final_aba + final_abc) % MOD
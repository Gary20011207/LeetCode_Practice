class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n, m = len(grid), len(grid[0])
        MOD = 10**9 + 7
        # sqrt(x^2 + 1^2) <=  d  => x^2 <= d^2 - 1
        # k: Max horizontal distance allowed when moving from row r+1 to r.
        k = int(max(0, d**2 - 1) ** 0.5)
        # up[c]: paths ending at grid[r][c] where the previous move was vertical (r+1 -> r)
        # shift[c]: paths ending at grid[r][c] where the previous move was horizontal (r -> r)
        up, shift = [0] * m, [0] * m
        # Iterate from bottom row to top row
        for r in reversed(range(n)):
            new_up, new_shift = [0] * m, [0] * m
            if r == n - 1:
                # Base case (Starting from any available cell in the bottom row)
                for c in range(m):
                    if grid[r][c] == '.':
                        new_up[c] = 1
            else:
                # Use prefix sums to calculate valid path totals from row r+1
                prev_total = [(up[i] + shift[i]) % MOD for i in range(m)]
                prefix = [0] * (m + 1)
                for i in range(m):
                    prefix[i + 1] = (prefix[i] + prev_total[i]) % MOD
                for c in range(m):
                    if grid[r][c] == '.':
                        # Horizontal range [c-k, c+k] for moving r+1 -> r
                        left, right = max(0, c - k), min(m - 1, c + k)
                        new_up[c] = (prefix[right + 1] - prefix[left]) % MOD
            # Horizontal Movement within the SAME row (r -> r)
            # Must follow a vertical move (cannot stay on the same row twice consecutively)
            new_prefix = [0] * (m + 1)
            for i in range(m):
                new_prefix[i+1] = (new_prefix[i] + new_up[i]) % MOD
            for c in range(m):
                if grid[r][c] == '.':
                    # Horizontal range [c-d, c+d] for moving within row r
                    left, right = max(0, c - d), min(m - 1, c + d)
                    total_range = (new_prefix[right + 1] - new_prefix[left]) % MOD
                    # Subtract new_up[c] because the move must be to a DIFFERENT cell
                    new_shift[c] = (total_range - new_up[c]) % MOD
            up, shift = new_up, new_shift
        # Result is the sum of all valid paths ending at any cell in the top row
        return sum((up[i] + shift[i]) for i in range(m)) % MOD
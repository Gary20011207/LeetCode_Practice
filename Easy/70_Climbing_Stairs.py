class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case
        if n < 2:
            return n
        # prev1 is dp[i - 2], prev2 is dp[i - 1]
        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            # Calculate next Fibonacci number (F(n) = F(n - 1) + F(n - 2))
            curr = prev1 + prev2
            # Update variables for the next step
            prev2, prev1 = curr, prev2
        
        return prev2
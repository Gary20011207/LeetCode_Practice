class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        # dp[0] = 0
        for i in range(1, n + 1):
            # The number of set bits in 'i' is:
            # 1. The number of set bits in 'i >> 1' (i / 2)
            # 2. Plus 1 if the last bit of 'i' is 1 (i & 1)
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp
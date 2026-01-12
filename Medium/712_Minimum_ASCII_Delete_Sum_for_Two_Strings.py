class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # dp[i][j] is the min cost for s1[0:i] and s2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # Base case (If s2 is empty, we must delete all of s1)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        # Base case (If s1 is empty, we must delete all of s2)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        # Fill the DP Table (Longest Common Subsequence)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match, no cost added
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Minimize cost by deleting from either s1 or s2
                    dp[i][j] = min(
                        # Delete from s1
                        dp[i - 1][j] + ord(s1[i - 1]),
                        # Delete from s2
                        dp[i][j - 1] + ord(s2[j - 1])
                    )
                    
        return dp[m][n]
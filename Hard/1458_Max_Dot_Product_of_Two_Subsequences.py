class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # dp[i][j] stores the max dot product using prefixes nums1[:i] and nums2[:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Product of current pair
                product = nums1[i - 1] * nums2[j - 1]
                # Maximize between four choices
                dp[i][j] = max(
                    # Start a new subsequence with only this pair
                    product,
                    # Extend the previous max dot product with this pair
                    product + dp[i - 1][j - 1],
                    # Skip current nums1 element
                    dp[i - 1][j],
                    # Skip current nums2 element
                    dp[i][j - 1]
                )

        return dp[n][m]
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Use Gauss's formula to find the difference between expected and actual sum
        return ((n * (n + 1)) // 2) - sum(nums)
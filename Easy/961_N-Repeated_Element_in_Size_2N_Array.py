class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Pigeonhole Principle
        # Max gap between N repeated elements is 2 (gap 3 for edge cases)
        for k in range(1, 4):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
        # Fallback
        return -1
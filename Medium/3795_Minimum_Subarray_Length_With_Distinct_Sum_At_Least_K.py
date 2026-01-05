from collections import defaultdict

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        # Track element frequencies in the window
        count = defaultdict(int)
        min_len = float("inf")
        l = 0
        # Sum of distinct elements in the current window
        total_sum = 0
        # Sliding window approach
        for r, num in enumerate(nums):
            # Add new distinct element to total_sum (Expand)
            count[num] += 1
            if count[num] == 1:
                total_sum += num
            # Try to minimize length while distinct sum condition is met (Shrink)
            while total_sum >= k:
                min_len = min(min_len, r - l + 1)
                # Remove from left and update sum if it was the last occurrence
                left_num = nums[l]
                count[left_num] -= 1
                if count[left_num] == 0:
                    total_sum -= left_num
                l += 1

        return min_len if min_len != float("inf") else -1
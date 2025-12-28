class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            complement = target - num
            # If the complement exists in the map, we found the pair
            if complement in seen:
                return [seen[complement], i]
            # Store the current number and its index in the map
            seen[num] = i
        # Fallback
        return []
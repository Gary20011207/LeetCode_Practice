class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                # Early Return (Found a duplicate)
                return True
            seen.add(num)

        return False
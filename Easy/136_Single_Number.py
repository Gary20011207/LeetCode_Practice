from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # reduce() cumulatively applies XOR across the list
        # Same numbers cancel out (x ^ x = 0), leaving the single one (x ^ 0 = x)
        return reduce(lambda x, y: x ^ y, nums)
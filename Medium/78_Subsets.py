class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start with the empty set
        res = [[]]
        for num in nums:
            # Double the subsets by adding 'num' to all existing ones (Cascading)
            res += [item + [num] for item in res]

        return res
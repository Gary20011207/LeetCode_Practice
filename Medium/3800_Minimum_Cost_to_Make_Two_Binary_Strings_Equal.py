class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        count_01, count_10 = 0, 0
        # Count mismatches
        for i in range(len(s)):
            if s[i] != t[i]:
                if s[i] == '0': count_01 += 1
                else: count_10 += 1
        # Best way to fix one '01' and one '10' (Swap s[i], s[j])
        cost_diff = min(2 * flipCost, swapCost)
        # Best way to fix two of the same type (Cross-swap one, then Swap s[i], s[j])
        cost_same = min(2 * flipCost, crossCost + swapCost)
        # Greedy pairing of opposite types
        pairs_diff = min(count_01, count_10)
        res = pairs_diff * cost_diff
        # Pair remaining mismatches of the same type
        remains = abs(count_01 - count_10)
        res += (remains // 2) * cost_same
        # If one single mismatch is left, the only option is to flip
        if remains % 2 == 1:
            res += flipCost

        return res
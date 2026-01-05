class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        # Total 2^n combinations
        num_masks = 1 << n
        # Cache for length and median of each mask to optimize DP
        total_len = [0] * num_masks
        medians = [0] * num_masks
        # Precompute total length and median for every possible mask
        for mask in range(1, num_masks):
            combined = []
            for i in range(n):
                if (mask >> i) & 1:
                    combined.extend(lists[i])
            combined.sort()
            total_len[mask] = len(combined)
            # Median is the left middle element per problem rules
            medians[mask] = combined[(len(combined) - 1) // 2]
        # dp[mask]: min cost to merge all lists represented by the mask
        dp = [float('inf')] * num_masks
        for mask in range(1, num_masks):
            # Base case (A single list requires no merges)
            if (mask & (mask - 1)) == 0:
                dp[mask] = 0
                continue
            # Efficiently iterate through all submasks (partitions) of the current mask
            sub = (mask - 1) & mask
            while sub > 0:
                remain = mask ^ sub
                # The cost of the final merge of these two subsets
                curr_merge_cost = total_len[mask] + abs(medians[sub] - medians[remain])
                dp[mask] = min(dp[mask], dp[sub] + dp[remain] + curr_merge_cost)
                # Move to next submask
                sub = (sub - 1) & mask
                
        return dp[num_masks - 1]
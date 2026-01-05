class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1_cost, prev2_cost = 0, 0
        # Iterate until the top of the floor (One step beyond cost array)
        for i in range(2, len(cost) + 1):
            curr_cost = min(prev1_cost + cost[i - 1], prev2_cost + cost[i - 2])
            prev2_cost = prev1_cost
            prev1_cost = curr_cost

        return prev1_cost
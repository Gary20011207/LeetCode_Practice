class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float("inf"), 0
        # Sliding Window Approach (min_price = l, price = r)
        for price in prices:
            if price < min_price:
                min_price = price
            # Calculate current profit and update max_profit if it's higher
            elif (price - min_price) > max_profit:
                max_profit = price - min_price

        return max_profit
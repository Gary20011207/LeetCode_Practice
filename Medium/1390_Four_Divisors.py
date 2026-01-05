class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        seen = dict()
        total_sum = 0

        for n in nums:
            if n in seen:
                total_sum += seen[n]
            else:
                count = 0
                div_sum = 0
                # Factors act in pairs (Square Root Optimization)
                for d in range(1, int(n ** 0.5) + 1):
                    if n % d == 0:
                        # Found the first divisor
                        count += 1
                        div_sum += d
                        # Add the paired divisor if it's not a perfect square
                        if d ** 2 != n:
                            count += 1
                            div_sum += n // d
                    # If more than 4 divisors, no need to continue
                    if count > 4:
                        break
                # Only p * q or p^3 have 4 divisors
                # Perfect squares always have odd divisor counts (never 4)
                seen[n] = div_sum if count == 4 else 0
                total_sum += seen[n]

        return total_sum
class Solution:
    def isHappy(self, n: int) -> bool:
        # Set to track visited numbers and detect cycles
        seen = set()
        # Stop if we reach 1 (Happy) or enter a loop (Not Happy)
        while (n != 1) and (n not in seen):
            seen.add(n)
            total_sum = 0
            # Extract digits mathematically to calculate square sum
            while n > 0:
                n, digit = n // 10, n % 10
                total_sum += digit ** 2
            n = total_sum
        # If n is 1, it's a happy number
        return n == 1
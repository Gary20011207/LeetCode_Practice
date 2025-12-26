class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # Brian Kernighan's Algorithm
        while n > 0:
            # Flip the least significant set bit (1) to 0
            n = n & (n - 1)
            # Increment count for each bit removed
            count += 1
            
        return count
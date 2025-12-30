class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # Shift res left and pull in n's LSB (Least Significant Bit)
            res = (res << 1) | (n & 1)
            # Move to next bit of n
            n >>= 1
            
        return res
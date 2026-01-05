class Solution:
    def canWinNim(self, n: int) -> bool:
        # You lose if the total number of stones is a multiple of 4
        return n % 4 != 0
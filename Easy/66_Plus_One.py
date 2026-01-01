class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate from right to left (Least Significant Digit)
        for i in range(len(digits) - 1, -1, -1):
            # No further carry needed
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # It becomes 0 (9 + 1 = 0) and carry continues
            digits[i] = 0
        # Case for all digits being 9
        return [1] + digits
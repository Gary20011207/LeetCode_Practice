class Solution:
    def largestEven(self, s: str) -> str:
        # Find the last '2' to ensure evenness and maximum length
        idx = s.rfind('2')
        return "" if idx == -1 else s[:idx + 1]
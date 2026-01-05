class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # s[:k]: Get the prefix of length k
        # [::-1]: Reverse the sliced prefix
        # s[k:]: Append the remaining part of the string
        return s[:k][::-1] + s[k:]
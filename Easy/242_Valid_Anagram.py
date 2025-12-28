from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case
        if len(s) != len(t):
            return False
        # Automatically handles missing keys with a default value of 0
        count = defaultdict(int)
        # Increment counts for string s
        for char in s:
            count[char] += 1
        # Decrement counts for string t
        for char in t:
            count[char] -= 1
        # All counts must be zero for it to be a valid anagram
        return all(val == 0 for val in count.values())
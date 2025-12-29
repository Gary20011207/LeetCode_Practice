class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and lowercase them
        s = "".join([c.lower() for c in s if c.isalnum()])
        # Initialize two pointers
        l, r = 0, len(s) - 1
        while l < r:
            # If characters don't match, it's not a palindrome
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
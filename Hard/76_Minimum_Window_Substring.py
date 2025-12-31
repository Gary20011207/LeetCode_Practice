import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if (not s) or (not t):
            return ""
        # Frequency of chars needed
        need = collections.Counter(t)
        # Total number of characters in t that must be covered
        missing = len(t)
        # Track best window ([length, start_index, end_index])
        res = [float("inf"), 0, 0]
        l = 0
        # Expand right pointer to find a valid window
        for r, char in enumerate(s):
            # If char is needed, decrease missing count
            if need[char] > 0:
                missing -= 1
            # Decrease frequency in need map
            need[char] -= 1
            # When all characters are covered, try to shrink from the left
            while missing == 0:
                # Update result if current window is smaller
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]
                # Recover char at left pointer
                need[s[l]] += 1
                # If the char was essential, we now need it again
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        # Return empty if no window found, else the sliced substring
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]
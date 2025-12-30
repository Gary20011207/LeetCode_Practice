class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char not in pair:
                # If it's an opening bracket, push to stack
                stack.append(char)
            else:
                # Must not be empty and must match the top element
                if (not stack) or (stack.pop() != pair[char]):
                    return False
        # Return True only if all brackets are matched   
        return not stack
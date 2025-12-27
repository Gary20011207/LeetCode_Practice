# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd Cycle Detection Algorithm (Tortoise and Hare Algorithm)
        slow, fast = head, head
        # Ensure we don't hit a None node
        while fast and fast.next:
            # Move slow pointer by 1 step
            slow = slow.next
            # Move fast pointer by 2 steps
            fast = fast.next.next
            # If they meet, there is a cycle
            if slow == fast:
                return True
        # If fast reaches the end, there is no cycle
        return False
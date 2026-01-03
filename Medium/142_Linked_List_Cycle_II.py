# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if (not head) or (not head.next):
            return None
        # Floyd Cycle Detection Algorithm (Tortoise and Hare Algorithm)
        slow, fast = head, head
        # Ensure we don't hit a None node
        while (fast) and (fast.next):
            slow = slow.next
            fast = fast.next.next
            # If they meet, there is a cycle
            if slow == fast:
                slow = head
                # Find the entry point of the cycle
                # L: dist to entry, d: dist from entry to meeting, C: loop length
                # 2 * Dist(slow) = Dist(fast) => 2(L + d) = L + nC + d
                # L = nC - d => Walking L steps from head and meeting point leads to entry.
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        # If fast reaches the end, there is no cycle
        return None
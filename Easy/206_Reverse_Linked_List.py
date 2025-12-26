# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # Iterative Approach
        while curr:
            # Store the next node
            nxt = curr.next
            # Reverse the link (1st round: Point to None to be Tail)
            curr.next = prev
            # Move prev forward
            prev = curr
            # Move curr forward
            curr = nxt
        # New head of the reversed list
        return prev
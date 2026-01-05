# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry_1 = 0
        while l1 or l2 or carry_1:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate sum and carry
            carry_1, out = divmod(val1 + val2 + carry_1, 10)
            # Append new node and move pointer
            curr.next = ListNode(out)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            # Compare and attach the smaller node
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # Move the tail pointer forward
            curr = curr.next
        # Attach the remaining portion of the non-empty list
        curr.next = list1 if list1 else list2
        # Return the actual head (Ignoring the dummy node)
        return dummy.next
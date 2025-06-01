# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        head = head.next
        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = curr

            if prev:
                prev.next = next

            prev = curr
            curr = curr.next

        return head

        
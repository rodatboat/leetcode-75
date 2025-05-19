# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        tort = head
        hare = head
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            if hare is tort:
                return True
        return False
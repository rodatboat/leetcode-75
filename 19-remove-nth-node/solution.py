# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        lptr = 0
        lptr_node = head

        rptr = 0
        curr = head
        while curr.next:
            curr = curr.next
            rptr += 1

            if rptr - lptr > n:
                lptr_node = lptr_node.next
                lptr+=1

        if n == rptr + 1:
            return head.next

        lptr_node.next = lptr_node.next.next if lptr_node.next else None
        return head    
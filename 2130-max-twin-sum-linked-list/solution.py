# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def pairSum(self, head: ListNode) -> int:
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        rev_head = self.reverse(slow)
        ans = 0
        while head and rev_head:
            ans = max(ans, head.val + rev_head.val)
            head = head.next
            rev_head = rev_head.next
        return ans
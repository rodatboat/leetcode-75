
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        # fast has to go double the slow
        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next
        return head
        
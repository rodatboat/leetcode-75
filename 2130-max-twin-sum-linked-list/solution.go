package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverse(head *ListNode) *ListNode {
	var prev *ListNode
	for head != nil {
		next := head.Next
		head.Next = prev
		prev = head
		head = next
	}
	return prev
}

func pairSum(head *ListNode) int {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// slow var contains the middle node
	rev_head := reverse(slow)
	ans := 0
	for head != nil && rev_head != nil {
		ans = max(ans, head.Val+rev_head.Val)
		head = head.Next
		rev_head = rev_head.Next
	}
	return ans
}

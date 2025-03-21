package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var prev *ListNode
	curr := head

	for curr != nil {
		aftr := curr.Next

		curr.Next = prev
		prev = curr

		curr = aftr
	}

	return prev
}

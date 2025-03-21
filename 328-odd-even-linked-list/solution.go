package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	odd := head
	oddh := head

	even := head.Next
	evenh := head.Next
	for even != nil && even.Next != nil {
		odd.Next = even.Next
		odd = odd.Next

		even.Next = odd.Next
		even = even.Next
	}

	odd.Next = evenh
	return oddh
}

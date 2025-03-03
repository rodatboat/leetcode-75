package main

type stack []int

func (s stack) Top() *int {
	if len(s) == 0 {
		return nil
	}
	return &s[len(s)-1]
}

func (s stack) Pop() (stack, *int) {
	if len(s) == 0 {
		return s, nil
	}
	return s[:len(s)-1], &s[len(s)-1]
}

func (s stack) Push(i int) stack {
	return append(s, i)
}

func removeStars(s string) string {
	return ""
}

package main

import (
	"strconv"
	"strings"
)

type stack []rune

func (s stack) Top() *rune {
	if len(s) == 0 {
		return nil
	}
	return &s[len(s)-1]
}

func (s stack) Pop() (stack, *rune) {
	if len(s) == 0 {
		return s, nil
	}
	return s[:len(s)-1], &s[len(s)-1]
}

func (s stack) Push(i rune) stack {
	return append(s, i)
}

func IsNum(i rune) bool {
	if int(i) >= 48 && int(i) <= 57 {
		return true
	}
	return false
}

func decodeString(s string) string {
	var stck stack
	for _, i := range s {
		if i != ']' {
			stck = append(stck, i)
		} else {
			var curr []rune
			for len(stck) > 0 && *stck.Top() != '[' {
				curr = append([]rune{*stck.Top()}, curr...)
				stck, _ = stck.Pop()
			}
			stck, _ = stck.Pop()

			var num []rune
			for len(stck) > 0 && IsNum(*stck.Top()) {
				num = append([]rune{*stck.Top()}, num...)
				stck, _ = stck.Pop()
			}

			n, _ := strconv.Atoi(string(num))
			currString := strings.Repeat(string(curr), n)
			stck = append(stck, []rune(currString)...)
		}
	}
	return string(stck)
}

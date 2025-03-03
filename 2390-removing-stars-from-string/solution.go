package main

import "fmt"

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

func removeStars(s string) string {
	var stck stack
	for _, i := range s {
		if i != '*' {
			stck = append(stck, i)
		} else {
			stck, _ = stck.Pop()
		}
	}

	return string(stck)
}

func main() {
	test1 := "leet**cod*e"
	test2 := "erase*****"

	fmt.Println(removeStars(test1))
	fmt.Println(removeStars(test2))
}

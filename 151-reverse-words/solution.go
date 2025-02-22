package main

import "strings"

func reverse(s []string) []string {
	l := len(s)
	for i := 0; i < l/2; i++ {
		s[i], s[l-1-i] = s[l-1-i], s[i]
	}
	return s
}

func reverseWords(s string) string {
	sArr := strings.Fields(s)
	sArr = reverse(sArr)
	return strings.Join(sArr, " ")
}

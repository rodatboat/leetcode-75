package main

import (
	"sort"
)

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	// Create maps of char to char frequency, we use array of 26 since it can only be a-z
	a1 := make([]int, 26)
	a2 := make([]int, 26)
	for _, i := range word1 {
		a1[i-'a']++
	}
	for _, i := range word2 {
		a2[i-'a']++
	}

	// check if chars are the same
	for idx, _ := range a1 {
		if (a1[idx] != 0 && a2[idx] == 0) || (a1[idx] == 0 && a2[idx] != 0) {
			return false
		}
	}

	// Sort list of frequencies (these should match)
	sort.Ints(a1)
	sort.Ints(a2)

	// Check if frequencies match
	for idx, _ := range a1 {
		if a1[idx] != a2[idx] {
			return false
		}
	}

	return true
}

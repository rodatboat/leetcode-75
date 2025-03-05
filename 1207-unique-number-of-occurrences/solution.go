package main

func uniqueOccurrences(arr []int) bool {
	s := make(map[int]int)
	for _, i := range arr {
		s[i]++
	}

	a := make(map[int]bool)
	for _, k := range s {
		a[k] = true
	}

	return len(a) == len(s)
}

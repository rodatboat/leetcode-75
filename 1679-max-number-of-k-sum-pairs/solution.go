package main

func maxOperations(nums []int, k int) int {
	a := make(map[int]int)
	op := 0
	for _, i := range nums {
		e := k - i
		if a[e] > 0 {
			a[e]--
			op++
		} else {
			a[i]++
		}
	}
	return op
}

package main

import (
	"math"
)

func increasingTriplet(nums []int) bool {
	mins := make([]int, 3)
	for i := range mins {
		mins[i] = math.MaxInt
	}

	for _, val := range nums {
		if val < mins[0] {
			mins[0] = val
		}
		if val > mins[0] {
			mins[1] = int(math.Min(float64(val), float64(mins[1])))
		}
		if val > mins[1] {
			return true
		}
	}

	return false
}

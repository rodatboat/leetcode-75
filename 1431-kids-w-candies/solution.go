package main

func max(arr []int) int {
	max_val := 0
	for _, val := range arr {
		if val > max_val {
			max_val = val
		}
	}

	return max_val
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	m := max(candies)
	var r []bool
	for _, val := range candies {
		if (val + extraCandies) >= m {
			r = append(r, true)
		} else {
			r = append(r, false)
		}
	}

	return r
}

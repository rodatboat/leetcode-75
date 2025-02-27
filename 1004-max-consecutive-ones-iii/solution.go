package main

func replaceZeros(k int, z_total int) int {
	if z_total <= k {
		return z_total
	} else {
		return k
	}
}

func longestOnes(nums []int, k int) int {
    r_total := 0
	z_total := 0
	a := 0
	lidx := 0
	for _, i := range nums {
		if i == 1 {
			r_total++
		} else {
			z_total++
		}

		if z_total > k {
			if nums[lidx] == 1 {
				r_total--
			} else {
				z_total--
			}
			lidx++
		}

		if r_total + replaceZeros(k, z_total) > a {
			a = r_total + replaceZeros(k, z_total)
		}
	}

	return a
}

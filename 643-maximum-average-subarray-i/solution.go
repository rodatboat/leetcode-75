package main

func findMaxAverage(nums []int, k int) float64 {
	var r_total float64 = 0.0
	var a float64 = 0.0
	for idx, i := range nums {
		if idx < k {
			r_total = r_total + float64(i)
			a = r_total / float64(k)
		} else {
			r_total = r_total - float64(nums[idx-k]) + float64(i)
			if r_total/float64(k) > a {
				a = r_total / float64(k)
			}
		}
	}
	return a

}

func moveZeroes(nums []int) {
	zero_count := 0
	writer_idx := 0
	for _, i := range nums {
		if i == 0 {
			zero_count++
		} else {
			nums[writer_idx] = i
			writer_idx++
		}
	}
	n := len(nums)
	for i := n - zero_count; i < n; i++ {
		nums[i] = 0
	}
}
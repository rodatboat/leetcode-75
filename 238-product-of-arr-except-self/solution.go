func initProdArr(size int) []int {
	arr := make([]int, size)
	for idx := range size {
		arr[idx] = 1
	}
	return arr
}
func productExceptSelf(nums []int) []int {
	size := len(nums)
	leftProds := initProdArr(size)
	rightProds := initProdArr(size)

	for idx := 1; idx < size; idx++ {
		leftProds[idx] = nums[idx-1] * leftProds[idx-1]
	}

	for idx := size - 2; idx > -1; idx-- {
		rightProds[idx] = nums[idx+1] * rightProds[idx+1]
	}

	for idx := range size {
		nums[idx] = leftProds[idx] * rightProds[idx]
	}

	return nums
}
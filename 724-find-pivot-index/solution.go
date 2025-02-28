package main

func pivotIndex(nums []int) int {
    n := len(nums)
    ridx := n - 1
    l_sum := make([]int, n)
    r_sum := make([]int, n)

    for idx, i := range nums {
        if idx == 0 {
            l_sum[idx] = i
            r_sum[ridx] = nums[ridx]
        } else {
            l_sum[idx] = i + l_sum[idx-1]
            r_sum[ridx] = r_sum[ridx+1] + nums[ridx]
        }
        ridx--
    }

    for i := 0; i < n; i++ {
        if l_sum[i] == r_sum[i] {
            return i
        }
    }
    return -1
}
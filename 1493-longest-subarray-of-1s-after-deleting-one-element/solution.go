package main

func longestSubarray(nums []int) int {
    z_total := 0
    r_total := 0
    lidx := 0
    a := 0
    for _, i := range nums {
        if i == 1 {
            r_total++
        } else {
            z_total++
        }
        if z_total > 1 {
            if nums[lidx] == 1 {
                r_total--
            } else {
                z_total--
            }
            lidx++
        }
        if r_total > a {
            if z_total == 0 {
                a = r_total - 1
            } else {
                a = r_total
            }
        }
    }

    return a
}
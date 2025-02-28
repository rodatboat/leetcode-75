package main

func findDifference(nums1 []int, nums2 []int) [][]int {
    n1 := make(map[int]int)
    n2 := make(map[int]int)

    for _, i := range nums1 {
        n1[i]++
    }
    for _, i := range nums2 {
        n2[i]++
    }

    a := make([][]int, 2)
    for k, _ := range n1 {
        if n2[k] == 0 {
            a[0] = append(a[0], k)
        }
    }

    for k, _ := range n2 {
        if n1[k] == 0 {
            a[1] = append(a[1], k)
        }
    }

    return a
}
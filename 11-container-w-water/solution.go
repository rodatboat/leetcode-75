package main

import (
    "math"
)

func maxArea(height []int) int {
    am := 0
    lidx := 0
    ridx := len(height) - 1
    for lidx < ridx {
        a := int(math.Min(float64(height[lidx]), float64(height[ridx]))) * int(ridx - lidx)
        if a > am {
            am = a
        }
        if height[lidx] < height[ridx] {
            lidx++
        } else {
            ridx--
        }
    }

    return am
}
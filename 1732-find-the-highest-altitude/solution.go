package main

func largestAltitude(gain []int) int {
    g := 0
    h := 0
    for _, i := range gain {
        g += i
        if g > h {
            h = g
        }
    }
    return h
}
package main

import (
	"math"
)


type stack []int

func (s stack) Top() *int {
    if len(s) == 0 {
        return nil
    }
    return &s[len(s)-1]
}

func (s stack) Pop() (stack, *int) {
	if len(s) == 0 {
        return s, nil
    }
    return s[:len(s)-1], &s[len(s)-1]
}

func (s stack) Push(i int) stack {
    return append(s, i)
}

func asteroidCollision(asteroids []int) []int {
	var s stack
    for _, i := range asteroids {
        for {
			top := s.Top()
			if top == nil {
				s = s.Push(i)
				break
			}

			if *top*i > 0 || i > 0 {
				s = s.Push(i)
				break
			} else {
				if math.Abs(float64(*top)) > math.Abs(float64(i)) {
					break
				} else if math.Abs(float64(*top)) == math.Abs(float64(i)) {
					s, _ = s.Pop()
					break
				} else {
					s, _ = s.Pop()
				}
			}
		}
    }
	return s
}
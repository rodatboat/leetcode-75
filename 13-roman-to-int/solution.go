package main

func romanToInt(s string) int {
	ak := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	a := 0
	sl := len(s)
	for idx, n := range s {
		k1 := ak[n]
		if idx < sl-1 && k1 < ak[rune(s[idx+1])] {
			a -= k1
		} else {
			a += k1
		}
	}

	return a
}

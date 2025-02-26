package main

func isVowel(r rune) bool {
	v := []rune{'a', 'e', 'i', 'o', 'u'}
	for _, vowel := range v {
		if vowel == r {
			return true
		}
	}
	return false
}

func maxVowels(s string, k int) int {
	r_total := 0
	a := 0
	for idx, i := range s {
		if idx < k {
			if isVowel(i) {
				r_total++
				a++
			}
		} else {
			if isVowel(i) {
				r_total++
			}
			if isVowel(rune(s[idx-k])) {
				r_total--
			}
			if r_total > a {
				a = r_total
			}
		}
	}
	return a
}

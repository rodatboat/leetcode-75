package main

func isSubsequence(s string, t string) bool {
	slen := len(s)
	tlen := len(t)
	if slen == 0 {
		return true
	}
	if tlen < slen {
		return false
	}
	sidx := 0
	for _, i := range t {
		if sidx < slen && i == rune(s[sidx]) {
			sidx++
		}
	}
	return sidx == slen
}

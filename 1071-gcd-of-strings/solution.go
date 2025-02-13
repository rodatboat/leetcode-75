import "strings"

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func gcdOfStrings(str1 string, str2 string) string {
	l1, l2 := len(str1), len(str2)
	r_size := gcd(l1, l2)
	r := str1[:r_size]

	f1, f2 := l1/r_size, l2/r_size

	if strings.Repeat(r, f1) == str1 && strings.Repeat(r, f2) == str2 {
		return r
	}
	return ""
}
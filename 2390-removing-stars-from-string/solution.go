package main

func removeStars(s string) string {
	res := make([]rune, len(s))
	widx := 0
	for _, i := range s {
		if i != '*' {
			res[widx] = i
			widx++
		} else {
			res[widx] = 0
			widx--
		}
	}
	return string(res[:widx])
}

func mergeAlternately(word1 string, word2 string) string {
	w1l := len(word1)
	w2l := len(word2)
	n := max(w1l, w2l)
	result := ""
	for idx := range make([]int, n) {
		if idx < w1l {
			result += string(word1[idx])
		}
		if idx < w2l {
			result += string(word2[idx])
		}
	}
	return result
}
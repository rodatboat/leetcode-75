import "slices"

func contains(slice []byte, char byte) bool {
	for _, i := range slice {
		if i == char {
			return true
		}
	}
	return false
}

func reverseVowels(s string) string {
	vowels := []byte{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	vList := []byte{}
	sArr := []byte(s)
	for _, val := range sArr {
		if contains(vowels, val) {
			vList = append(vList, val)
		}
	}
	slices.Reverse(vList)

	vIdx := 0
	for idx, val := range sArr {
		if contains(vowels, val) {
			sArr[idx] = vList[vIdx]
			vIdx += 1
		}
	}

	return string(sArr)
}
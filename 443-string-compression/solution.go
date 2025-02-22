package main

import (
	"strconv"
)

func compress(chars []byte) int {
	resStr := ""
	var groupLetter *byte = nil
	var groupCount int = 0
	for idx, letter := range chars {
		if groupLetter != nil && letter == *groupLetter {
			groupCount += 1
		}
		if groupLetter == nil {
			groupLetter = &letter
			groupCount = 1
		}
		if idx == len(chars)-1 || chars[idx+1] != letter {
			resStr += string(*groupLetter)
			if groupCount > 1 {
				resStr += strconv.Itoa(groupCount)
			}
			groupLetter = nil
			groupCount = 0
		}
	}
	resBytes := []byte(resStr)
	copy(chars, resBytes)
	return len(resBytes)
}

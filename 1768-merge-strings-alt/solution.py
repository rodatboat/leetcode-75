class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1l = len(word1)
        w2l = len(word2)
        result = ""
        for idx in range(0, max(w1l, w2l)):
            if idx < w1l:
                result += word1[idx]
            if idx < w2l:
                result += word2[idx]
        return result
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        a = strs[0]
        for i in range(len(a)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != a[i]:
                    return a[:i]
        return a
        
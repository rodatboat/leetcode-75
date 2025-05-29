class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        rev = []
        for i in range(len(a)):
            rev.append(a[i])
            if i > 0:
                rev.append("")
        return " ".join(reversed(a))
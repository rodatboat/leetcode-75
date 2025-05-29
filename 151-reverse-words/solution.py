class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        rev = []
        for i in range(len(a)-1, -1, -1):
            rev.append(a[i])
        return " ".join(rev)
class Solution:
    def reverseWords(self, s: str) -> str:
        sArr = [i for i in s.split(" ") if i.strip()]
        sArr.reverse()
        return ' '.join(sArr)
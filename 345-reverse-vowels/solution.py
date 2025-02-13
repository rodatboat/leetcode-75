class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vList = [i for i in s[::-1] if i in vowels]
        vIdx = 0
        cList = list(s)
        for idx, i in enumerate(cList):
            if i in vowels:
                cList[idx] = vList[vIdx]
                vIdx += 1
        return ''.join(cList)
                
        
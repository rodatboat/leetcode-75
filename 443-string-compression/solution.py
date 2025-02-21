class Solution:
    def compress(self, chars: List[str]) -> int:
        resStr = ""
        groupLetter = ''
        groupSize = 0
        for idx, i in enumerate(chars):
            if i == groupLetter:
                groupSize += 1
            if groupLetter == '':
                groupLetter = i
                groupSize = 1
            if idx == len(chars)-1 or chars[idx+1] != i:
                resStr += i
                if groupSize > 1:
                    resStr += str(groupSize)
                groupLetter = ''
                groupSize = 0
        chars[:] = ''.join(resStr)
        return len(chars)
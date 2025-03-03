class Solution:
    def getTop(self, stack: list[int]) -> int:
        top = stack[-1] if stack else None
        return top

    def isLetter(self, s:str) -> bool:
        if ord(s) >= 97 and ord(s) <= 122:
            return True
        return False

    def isNum(self, s:str) -> bool:
        if ord(s) >= 48 and ord(s) <= 57:
            return True
        return False

    def decodeString(self, s: str) -> str:
        a = []
        for i in range(len(s)):
            if s[i] != ']':
                a.append(s[i])
            else:
                curr = []
                while a and a[-1] != '[':
                    curr.insert(0, a.pop())
                a.pop() # remove "["
                
                num = []
                while a and self.isNum(a[-1]):
                    num.insert(0, a.pop())

                n = int("".join(num))
                a.extend("".join(curr) * n)
        return "".join(a)
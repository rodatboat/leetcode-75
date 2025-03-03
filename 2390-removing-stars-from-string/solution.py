class Solution:
    def getTop(self, stack: list[int]) -> int:
        top = stack[-1] if stack else None
        return top

    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
        

s = Solution()

test1 = "leet**cod*e"
test2 = "erase*****"

print(s.removeStars(test1))
print(s.removeStars(test2))
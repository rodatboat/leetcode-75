class Solution:
    def getTop(self, stack: List[int]) -> int:
        top = stack[-1] if stack else None
        return top

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = []
        for idx, i in enumerate(asteroids):
            while True:
                top = self.getTop(a)
                if top == None or top*i > 0:
                    a.append(i)
                    break

                if i > 0:
                    a.append(i)
                    break
                else:
                    if abs(top) > abs(i):
                        break
                    elif abs(top) == abs(i):
                        a.pop()
                        break
                    else:
                        a.pop()
        return a
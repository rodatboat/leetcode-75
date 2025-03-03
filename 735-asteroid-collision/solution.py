class Solution:
    def getTop(self, stack: List[int]) -> int:
        top = stack[-1] if stack else None
        return top

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = []
        for idx, i in enumerate(asteroids):
            while True:
                top = self.getTop(a)
                if i > 0 or top == None or top*i > 0:
                    a.append(i)
                    break
                if abs(top) > abs(i):
                    # if top is gt, it wins, so dont add i to stack
                    break
                elif abs(top) == abs(i):
                    a.pop()
                    # if top == i, its a draw. a is (--) from the stack, and i never gets (++) to stack top
                    break
                else:
                    # if 
                    a.pop()
        return a
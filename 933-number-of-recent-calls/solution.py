from collections import deque

class RecentCounter:

    def __init__(self):
        self.c = deque()

    def ping(self, t: int) -> int:
        self.c.append(t)
        r = [t - 3000, t]
        while self.c and self.c[0] < r[0]:
            self.c.popleft()

        return len(self.c)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
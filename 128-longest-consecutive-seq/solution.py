from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        a = 0
        dq = deque()
        for i in s:
            if len(dq) == 0:
                dq.append(i)
            elif dq[-1] + 1 == i:
                dq.append(i)
            else:
                dq.clear()
                dq.append(i)
            if len(dq) > a:
                a = len(dq)
        return a
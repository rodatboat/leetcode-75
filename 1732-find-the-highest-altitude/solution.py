class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g = 0
        h = 0
        for idx, i in enumerate(gain):
            g += i
            if g > h:
                h = g
        return 0 if h < 0 else h

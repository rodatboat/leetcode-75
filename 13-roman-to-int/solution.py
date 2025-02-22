class Solution:
    def romanToInt(self, s: str) -> int:
        ak = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        a = 0
        queue = []
        for ridx, i in enumerate(s): # loop through s, and use read index
            queue.append(i)
            k1 = ak[queue[0]]
            if len(queue) == 2:
                k2 = ak[queue[1]]
                if k1 < k2:
                    a += k2 - k1
                    queue.pop(0)
                    queue.pop(0)
                else:
                    a += k1
                    queue.pop(0)
            if ridx == len(s)-1:
                for i in queue:
                    a += ak[i]
                    queue.pop(0)
        return a

            
        
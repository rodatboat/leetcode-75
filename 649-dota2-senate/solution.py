from collections import deque

class Solution:
    # Recommended approach uses queue. Use 'deque' for O(1) dequeue using popleft()
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r = deque()
        d = deque()

        # store all the senators into their respective party's queue, but store their indexes, the count is length of queue
        for idx, i in enumerate(senate):
            if i == 'D':
                d.append(idx)
            else:
                r.append(idx)

        # loop until one of the queues is empty
        while r and d:
            r_idx = r.popleft()
            d_idx = d.popleft()
            # check which senator's index is smaller (aka which comes first in the line, and takes priority)
            if r_idx < d_idx:
                # if rad goes first, add it to the back of the queue, and the dire that lost the condition stays out...
                r.append(r_idx + n)
            else:
                d.append(d_idx + n)
        
        return "Radiant" if r else "Dire"
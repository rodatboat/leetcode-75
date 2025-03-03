class Solution:
    # Recommended approach uses queue. 
    # Enqueue is append, Dequeue is pop(0)

    def senateRound(self, senate: str) -> str:
        queue = [i for i in senate]
        # bans pending
        d = 0
        r = 0
        while True:
            ban_queue = []
            for idx, i in enumerate(queue):
                if i == 'D':
                    if r == 0:
                        d += 1
                    else:
                        ban_queue.append(idx)
                        r -= 1
                else:
                    if d == 0:
                        r += 1
                    else:
                        ban_queue.append(idx)
                        d -= 1

            banned = False
            while ban_queue:
                banned = True
                queue.pop(ban_queue.pop())
            
            if not banned:
                break
                
        if d > 0:
            return "Dire"
        else:
            return "Radiant"
        

s = Solution()

test1 = "RD" # Radiant
test2 = "RDD" # Dire
test3 = "DDRRR" # Dire

print(s.senateRound(test1))
print(s.senateRound(test2))
print(s.senateRound(test3))
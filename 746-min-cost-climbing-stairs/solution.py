class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # [10,15,20,0]
        n = len(cost)
        
        for i in range(n-4, -1, -1): # we do -4, because the we want to start before the last 2 steps, which are ez. 
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])

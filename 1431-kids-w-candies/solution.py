class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r = []
        max_r = max(candies)
        for idx, i in enumerate(candies):
            add = i + extraCandies
            if add >= max_r:
                r.append(True)
            else:
                r.append(False)

        return r
        
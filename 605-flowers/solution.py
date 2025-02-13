class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        r = 0
        q = 0
        for i in flowerbed:
            if q == 3 or (r > 0 and q == 3):
                r += 1
                q = 0
            q += 1
            if flowerbed[i] == 1:
                q = 0
        return r >= n
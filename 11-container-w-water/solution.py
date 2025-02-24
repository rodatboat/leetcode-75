class Solution:
    def maxArea(self, height: List[int]) -> int:
        # get area where x => idx, and y => height
        am = 0
        lidx = 0
        ridx = len(height)-1

        while lidx <= ridx:
            a = min(height[lidx], height[ridx]) * (ridx-lidx)
            if a > am:
                am = a
            if height[lidx] > height[ridx]:
                ridx -= 1
            else:
                lidx += 1
        return am
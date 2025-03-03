class Solution:
    def getTop(self, stack: List[int]) -> int:
        top = stack[-1] if stack else None
        return top
        
    def removeStars(self, s: str) -> str:
        
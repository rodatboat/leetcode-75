class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for s in strs:
            chars = sorted(s)
            chars = "".join(chars)
            if chars not in solution:
                solution[chars] = []
            solution[chars].append(s)

        return [s for s in solution.values()]

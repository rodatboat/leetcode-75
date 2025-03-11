from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a1 = Counter(word1)
        a2 = Counter(word2)

        if len(word1) != len(word2):
            return False
        
        return a1.keys() == a2.keys() and sorted(a1.values()) == sorted(a2.values())
class Solution:
    def tribonacci(self, n: int) -> int:
        self.a = {}


        def calculateTribonacci(i: int):
            if i in self.a:
                return self.a[i]

            if i == 0:
                return 0
            elif i == 1 or i == 2:
                return 1
            else:
                answer = calculateTribonacci(i-1) + calculateTribonacci(i-2) + calculateTribonacci(i-3)
                self.a[i] = answer
                return answer

        return calculateTribonacci(n)


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n + 1):
            t = i
            while t:
                t &= (t - 1)
                output[i] += 1
        return output


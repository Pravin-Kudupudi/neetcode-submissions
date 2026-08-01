class Solution:
    def reverseBits(self, n: int) -> int:
        bit = ""

        for i in range(32):
            if n & (1 << i):
                bit += "1"
            else:
                bit += "0"
        
        res = 0
        for i, bit in enumerate(bit[::-1]):
            if bit == "1":
                res |= (1 << i)
        
        return res
        
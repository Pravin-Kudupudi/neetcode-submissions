class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums

    def sumRange(self, left: int, right: int) -> int:
        l, r, sum = left, right, 0

        while l < r:
            sum += self.array[l] + self.array[r]
            l += 1
            r -= 1
        
        if l == r:
            sum += self.array[l]
            
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        sum = 0
        for i in range(1, len(nums) + 1):
            sum += nums[i - 1]
            self.prefix[i] = sum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
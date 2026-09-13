class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        target = len(nums) // 2

        for n in nums:
            if count.get(n, 0) == target:
                return n
            count[n] = 1 + count.get(n, 0)
        return -1
        
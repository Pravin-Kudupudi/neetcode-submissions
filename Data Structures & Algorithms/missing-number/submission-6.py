class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total =  (len(nums) * (len(nums) + 1)) // 2
        sumation = 0

        for n in nums:
            sumation += n
        
        return total - sumation

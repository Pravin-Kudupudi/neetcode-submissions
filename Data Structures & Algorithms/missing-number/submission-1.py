class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        trueSum = self.calcSum(len(nums))
        newSum = 0

        for i in range(len(nums)):
            newSum += nums[i]
        
        return trueSum - newSum

    
    def calcSum(self, n: int) -> int:
        res = 0
        for i in range(n + 1):
            res += i
        return res
        
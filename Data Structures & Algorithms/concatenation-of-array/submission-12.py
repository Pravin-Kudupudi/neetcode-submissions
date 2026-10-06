class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       ans = [0] * (len(nums) * 2)
       length = len(nums)

       for i in range(len(nums)):
          ans[i] = nums[i]
          ans[i + length] = nums[i]
        
       return ans
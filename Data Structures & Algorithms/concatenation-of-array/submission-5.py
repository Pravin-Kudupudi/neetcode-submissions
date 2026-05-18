class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        l = len(nums)

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + l] = n
        
        return ans
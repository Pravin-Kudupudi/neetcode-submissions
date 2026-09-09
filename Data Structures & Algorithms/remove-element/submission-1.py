class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < k:
            if type(nums[i]) is int and nums[i] == val:
                k -= 1
                nums[i] = nums[k]
            else:
                i += 1
        return k
        # for i in range(len(nums) - 1, -1, -1):
        #     print(nums[i])
        #     print(nums[i] == val)
        #     if nums[i] == val:
        #         nums[i] = "_"
        #         k -= 1
        #     print(nums)
        # return k
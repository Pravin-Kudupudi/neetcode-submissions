class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: # 1, 2
            if nums[l] == val: # 2, 3
                nums[l], nums[r] = nums[r], '_' # 3, 3 = 3, '_' arr = [3, 2, 2, '_']
                r -= 1
            else:
                l += 1
        
        return l
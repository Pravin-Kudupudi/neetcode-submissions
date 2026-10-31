func sortColors(nums []int) {
	l, i, r := 0, 0, len(nums) - 1

	for i <=r {
		if nums[i] == 0 {
			nums[l], nums[i] = nums[i], nums[l]
			l++
		} else if nums[i] == 2 {
			nums[r], nums[i] = nums[i], nums[r]
			r--
			i--
		}
		i++
	}
}

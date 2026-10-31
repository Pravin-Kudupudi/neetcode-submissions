func validPalindrome(s string) bool {
	l, r := 0, len(s) - 1

	for l < r {
		if s[l] == s[r] {
			l++
			r--
		} else {
			return isPal(l + 1, r, s) || isPal(l, r - 1, s)
		}
	}
	return true
}

func isPal(l, r int, s string) bool {
	for l < r {
		if s[l] == s[r]{
			l++
			r--
		} else {
			return false
		}
	}
	return true
}
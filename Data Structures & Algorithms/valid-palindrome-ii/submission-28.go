func validPalindrome(s string) bool {
	l, r := 0, len(s) - 1

	for l < r {
		if s[l] != s[r] {
			return isPal(l + 1, r, s) || isPal(l, r - 1, s)
		}
		l++
		r--
	}
	return true
}

func isPal(l, r int, s string) bool {
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}
	return true
}
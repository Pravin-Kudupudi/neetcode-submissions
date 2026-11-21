/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func serialize(root *TreeNode) string {
	var res strings.Builder

	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			res.WriteString("$#")
			return
		}
		res.WriteString("$")
		res.WriteString(strconv.Itoa(node.Val))
		dfs(node.Left)
		dfs(node.Right)
	}

	dfs(root)
	return res.String()
}

func zFunction(s string) []int {
	n := len(s)
	z := make([]int, n)
	l, r := 0, 0

	for i := 1; i < n; i++ {
		if i <= r {
			z[i] = min(z[i - l], r-i+1)
		}
		for i + z[i] < n && s[z[i]] == s[i + z[i]] {
			z[i]++
		}
		if i + z[i] - 1 > r {
			l = i
			r = i + z[i] - 1
		}
	}

	return z
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	rootSer := serialize(root)
	subRootSer := serialize(subRoot)
	combined := subRootSer + "|" + rootSer

	subLen := len(subRootSer)
	z := zFunction(combined)

	for i := subLen - 1; i < len(combined); i++ {
		if z[i] == subLen {
			return true
		}
	}
	return false
}

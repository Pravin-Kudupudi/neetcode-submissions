type MinHeap [][2]int

func (h MinHeap) Len() int				{ return len(h) }
func (h MinHeap) Less(i, j int) bool 	{ return h[i][0] < h[j][0] }
func (h MinHeap) Swap(i, j int)			{ h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{})	{ *h = append(*h, x.([2]int)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n - 1]
	*h = old[:n - 1]
	return x
}

func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)
	for _, num := range nums {
		count[num]++
	}

	minHeap := &MinHeap{}
	heap.Init(minHeap)

	for key, value := range count {
		heap.Push(minHeap, [2]int{value, key})
		if minHeap.Len() > k {
			heap.Pop(minHeap)
		}
	}

	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = heap.Pop(minHeap).([2]int)[1]
	}

	return res
}

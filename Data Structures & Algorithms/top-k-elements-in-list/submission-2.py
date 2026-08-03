class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)

        for n in nums:
            store[n] += 1
        
        arr = []
        for key, value in store.items():
            arr.append((value, key))
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
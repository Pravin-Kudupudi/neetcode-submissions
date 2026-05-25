class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profMap = {}

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profMap.get(prices[i], 0) < profit:
                    profMap[prices[i]] = profit
        
        ans = 0
        for n in profMap.values():
            ans = max(n, ans)
        
        return ans


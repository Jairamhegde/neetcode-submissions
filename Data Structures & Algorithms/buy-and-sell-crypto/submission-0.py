class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_element = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_element:
                min_element = prices[i]
            else:
                max_profit = max(max_profit,prices[i] - min_element)
        return max_profit

        
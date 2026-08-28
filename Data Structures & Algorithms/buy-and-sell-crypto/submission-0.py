class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        best = 0

        while left < len(prices) - 1:
            if prices[left] < prices[right]:
                curRight = right
                curHighest = right
                while curRight < len(prices):
                    if prices[curRight] > prices[curHighest]:
                        curHighest = curRight
                    curRight += 1
                curProfit = prices[curHighest] - prices[left]
                if curProfit > best:
                    best = curProfit

            left += 1
            right += 1
        
        return best
                    
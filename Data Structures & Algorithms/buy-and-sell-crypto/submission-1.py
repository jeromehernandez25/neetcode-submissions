class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        best = 0

        # Iterate until left has been all values except last in prices array
        while left < len(prices) - 1:
            # If left index value less that right index value
            if prices[left] < prices[right]:
                # Create running indexes for current right index and highest value right index
                curRight = right
                curHighest = right
                # Use running indexes to find highest value from right index till end of array
                while curRight < len(prices):
                    if prices[curRight] > prices[curHighest]:
                        curHighest = curRight
                    curRight += 1
                # Use highest value to calculate current best profit for this left index value
                curProfit = prices[curHighest] - prices[left]
                # If current profit better than best profit, replace
                if curProfit > best:
                    best = curProfit

            # Increment left and right counter
            left += 1
            right += 1
        
        return best
                    
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = -1
        
        # Have two pointers from each end of the array converge
        # For each positioning of the two pointers, calculate the 
        # current amount of water that can be held, if the current amount 
        # is greater than the current best, record the current amount instead
        l = 0
        r = len(heights) - 1
        while l < r:
            left = heights[l]
            right = heights[r]
            
            cur_height = (r - l) * min(left, right)
            if cur_height > best:
                best = cur_height

            # Take the local best action which is to keep the higher bar between
            # the left and right pointer
            if left > right:
                r -= 1
            else:
                l += 1
        
        return best

            


        
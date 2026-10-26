class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Keep running count for characters in the sliding window.
        # Each iteration, for the current sliding window, check if total char count
        # minus most popular char count is greater than k.
        # If greater than k, window invalid so remove character at l from count 
        # and increment l

        best = 0
        l = 0
        count = {}

        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1

            # Invalid window: remove the character at and increment l
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            best = max(best, r - l + 1)
            
        
        return best
            
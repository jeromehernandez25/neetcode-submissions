class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Parse string s with for lowercased alphanumeric characters
        clean_string = []
        for c in s:
            if c.isalnum():
                clean_string.append(c.lower())
        
        # Use two pointers from each end of the parsed string
        # and compare until they intersect or if a
        # mismatch between characters is found
        l, r = 0, len(clean_string) - 1
        while l < r:
            if clean_string[l] != clean_string[r]:
                return False
            l += 1
            r -= 1
        
        return True

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Trivial solution would be to count the number of times
        # an integer appears and return the integer with a count of 1
        # Problem is that this takes O(n) time and O(n) space

        # Instead, since every integer appears twice except for one,
        # we can XOR every element together, cancelling all of the 
        # integers that appear twice, leaving us with the integer
        # that only appears once. This gives O(n) time with O(1) space

        res = 0
        for n in nums:
            res = res ^ n
        
        return res

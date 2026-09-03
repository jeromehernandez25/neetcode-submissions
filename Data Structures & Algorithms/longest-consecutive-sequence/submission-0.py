class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Trivial O(n log n) solution would be to sort the array and then iterate through,
        # saving the longest sequence

        # Take advantage of the fact that without sorting the array, we can put the array
        # into a hashset, then find where a sequence starts, and count its length from there
        # saving the longest sequence

        # Create hashset from nums array and longest variable to save longest sequence
        hashSet = set(nums)
        longest = 0

        # Iterate through each number in hashSet
        for n in hashSet:
            # If the current number minus 1 does not exist in hashSet, 
            # then the current number is the start of a sequence
            if (n - 1) not in hashSet:
                
                # Count how long the current sequence is
                length = 1
                while (n + length) in hashSet:
                    length += 1
                
                # Save the longest sequence 
                longest = max(longest, length)
        
        return longest

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Set two pointers the the start and end of nums array
        l = 0
        r = len(nums) - 1

        # Initialize last_lowest variable which will hold the last known lowest value found
        last_lowest = nums[0]

        # Binary search loop to find minimum value until left and right boudnary intersect
        while l <= r:
            # Get middle value
            middle = (l + r) // 2

            # If middle value is less than or equal to the last element, new lowest found so record it
            # Also move the right boundary to the lef tof middle value to search remaining half of array
            if nums[middle] <= nums[-1]:
                last_lowest = nums[middle]
                r = middle - 1
            # Middle value is bigger than last element's value so search right part of the array
            else:
                l = middle + 1
        
        # Return the lowest value found
        return last_lowest
            
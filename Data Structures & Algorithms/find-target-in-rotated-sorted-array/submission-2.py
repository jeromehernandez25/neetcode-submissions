class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Write an algorithm to find where the break/rotation occurs
        # Then use a binary search algorithm on the portion that contains the target

        # Set two pointers the the start and end of nums array
        l = 0
        r = len(nums) - 1

        # Low index variable to hold the index of the lowest value in array
        low_index = 0

        # Binary search loop to find minimum value until left and right boundary intersect
        while l <= r:
            middle = (l + r) // 2
            
            if nums[middle] == target:
                return middle
            # Middle value is bigger than last element so search right part of the array for break
            elif nums[middle] > nums[-1]:
                l = middle + 1
            # Middle value less than or equal to the last element, new lowest found so record it
            # And search left part of the array for break
            else:
                low_index = middle
                r = middle - 1
        
        # Break found, now adjust left and right pointers to the array partition that possibly contains target 
        if target > nums[-1]:
            l = 0
            r = low_index - 1
        else:
            l = low_index
            r = len(nums) - 1
        
        # Binary search on array partition that could cotain target
        while l <= r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        
        return -1


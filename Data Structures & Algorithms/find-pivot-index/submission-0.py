class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Take advantage of the fact that when iterating through the list
        # looking for the pivot value, the values on the left side of the pivot
        # are always adding the previous value from the previous iteration

        # Get total of array
        total = sum(nums)

        # Running counter for left_sum from current pivot
        left_sum = 0        

        # For each possible pivot value, calculate and compare to see
        # if left_sum is equal to right_sum and return current index if true
        # Update left_sum value if not
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]

        # Pivot value does not exist
        return -1
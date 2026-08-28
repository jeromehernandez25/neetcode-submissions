class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Keep left and right indexes which indicate the ends of the current search list
        l, r = 0, len(nums) - 1

        # Iterate until left and right boundaries cross each other
        while l <= r:
            # Get middle of current search list
            middle = (l + r) // 2

            # If middle index is target, return middle index
            if nums[middle] == target:
                return middle
            # If middle index bigger than target, target is in lower half of list
            # So update the right boundary to be just below the middle index
            elif nums[middle] > target:
                r = middle - 1
            # If middle index smaller than target, target is in upper half of list
            # So update the left boundary to be just above the middle index
            else:
                l = middle + 1
        
        # Entire list was iterated through and target value not in list
        return -1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort numbers in order, then for each element, use two pointers
        # that converge to find the triplets that add up to zero for each element
        ans = []
        nums.sort()

        for index, value in enumerate(nums):
            # If nums is assorted in ascending order and value is positive, 
            # then remaining values cannot add to get 0
            if value > 0: 
                break
            
            # If this number is the same as the previous, there will be a duplicate
            # result, so skip this iteration
            if index > 0 and value == nums[index - 1]:
                continue
            
            # Use two pointers to iterate from each end of the array
            # to find the unique triplets that add up to 0 for this index
            l = index + 1
            r = len(nums) - 1
            while l < r:
                result = value + nums[l] + nums[r]

                # If result is above 0, move right pointer down to reduce sum
                # and move left pointer up if below 0
                if result > 0:
                    r -= 1
                elif result < 0:
                    l += 1
                # If answer found, append triplet to ans array and 
                # move the two pointers 1 element inwards and 
                # move the left pointer so that it does not process duplicate values
                else:
                    ans.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return ans

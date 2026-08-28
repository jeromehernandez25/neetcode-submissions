class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Idea: For each element except the last,, do binary serach on the remaining
        # right side of the array to find the complement of the current element
        
        size = len(numbers)

        # If size of array is less than two, no sum can be made, return empty
        if size < 2:
            return []
        
        # If array size is 2 and there is always 1 valid solution, 
        # return the only 2 indices
        if size == 2:
            return [1, 2]

        # Iterate through each element in the array except the last element
        # Use enumerate so that we can keep track of the index of the element
        for index, value in enumerate(numbers[:-1]):

            # Calculate the complement of the current element that we will look for
            # in the while loop
            complement = target - value

            # Calculate l and r which will be our running bounds for the while loop
            l = index + 1
            r = size - 1

            # Run while loop until l and r bounds intersect
            while l <= r:
                # Calculate middle value between l and r boundaries
                middle = (l + r) // 2
                
                # If middle value is complement, then return the index of the
                # current index and the index of the complement
                if numbers[middle] == complement:
                    return [index + 1, middle + 1]
                
                # If middle value is more than complement, then complement cannot be
                # in the higher half, move boundary r to left of middle
                elif numbers[middle] > complement:
                    r = middle - 1
                
                else:
                    l = middle + 1
        
        # If this point is reached, complement does not exist in array so return empty
        return []


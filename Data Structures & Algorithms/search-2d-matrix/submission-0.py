class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m rows and n colums
        # Save top and bottom rows as 
        # Get middle row
        # Check if middle row starting value is target
        # If row starting value more than target, search 1st half of rows
        # If row starting value less than target, search 2nd half of rows
        # 
        
        # Get length of rows and columns in matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Use binary search to find which row target is in
        top_row = 0
        bottom_row = rows - 1
        while top_row <= bottom_row:
            middle_row = (bottom_row + top_row) // 2

            # Check starting value in row
            if matrix[middle_row][0] == target:
                return True
            elif matrix[middle_row][0] > target:
                bottom_row = middle_row - 1
            else:
                top_row = middle_row + 1
        
        # Bottom row is row with target in it
        # if it is 0 or less, than target does not exist
        target_row = bottom_row
        if target_row < 0: 
            return False
        
        # Standard 1D dbinary search to find target value
        left = 0
        right = cols - 1
        while left <= right:
            middle_col = (left + right) // 2

            if matrix[target_row][middle_col] == target:
                return True
            elif matrix[target_row][middle_col] > target:
                right = middle_col - 1
            else:
                left = middle_col + 1
        
        # Target value not found in any row or column in matrix
        return False
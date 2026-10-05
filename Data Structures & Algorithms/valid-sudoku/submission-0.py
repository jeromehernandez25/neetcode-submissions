class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each 3x3 sub-box to make sure there are no duplicates of any digits
        # Create an empty set for each sub-box, skipping empty squares, adding new digits
        # to the set, and returning false if a digit is already within the set
        subBoxLength = 3
        for square in range(len(board)):
            seen = set()
            for i in range(subBoxLength):
                for j in range(subBoxLength):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    
                    if board[row][col] in seen:
                        return False
                    
                    seen.add(board[row][col])

        # Check if rows have any duplicates
        # Similar logic to sub-box where if a digit already exists within the set
        # we return false, otherwise add to set seen
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in seen:
                    return False

                seen.add(board[row][col])

        # Check if cols have any duplicate
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in seen:
                    return False
                    
                seen.add(board[row][col])

        # All sub-boxes, rows, and cols have no duplicates, return True
        return True

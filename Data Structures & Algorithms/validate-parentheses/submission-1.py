class Solution:
    def isValid(self, s: str) -> bool:
        stack = []      # Stack to hold opening brackets
        dictionary = {  # Dictionary for closed bracket comparisons
            "[": "]",
            "(": ")",
            "{": "}"
        }
        opening_brackets = set("[({") # Variable for finding open brackets

        for char in s:              # Iterate through entire string
            if char in opening_brackets: # If current char is an open bracket
                stack.append(char);      # Append it to the stack
            else:
                if not stack: # Check to see that stack is not empty
                    return False
                
                popped = stack.pop()     # Else get the stack's top element
                if dictionary[popped] is not char: # If char doesn't close popped open bracket
                    return False            # Then return False
        
        if stack: # Return false if open brackets still left in stack
            return False

        return True # Iterated entire string and no open brackets left
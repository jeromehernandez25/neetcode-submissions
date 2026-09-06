class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize stack to hold terms, and set of valid operators
        valid_operators = {'+', '-', '*', '/'}
        stack = []
        
        # Iterate through each token in tokens
        for token in tokens:
            # If token is an operator, then perform operation on
            # the top 2 terms in the stack
            if token in valid_operators:
                t2 = stack.pop()
                t1 = stack.pop()

                # Perform operation according to operand poppped
                # and append result back onto the stack
                if token == "+":
                    stack.append(t1 + t2)
                elif token == "-":
                    stack.append(t1 - t2)
                elif token == "*":
                    stack.append(t1 * t2)
                else:
                    stack.append(int(t1 / t2))
            # If token is not an operator, append term to top of stack
            else:
                stack.append(int(token))
        
        return stack.pop()

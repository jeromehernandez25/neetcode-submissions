class MinStack:

    def __init__(self):
        # Hold two stacks, 1 for original stack, 
        # And the other keeps track of the lowest value at each level/element in the stack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push val onto stack as normal
        self.stack.append(val)

        # If min_stack has an element, append the lowest between val and min_stack's
        # top element and append the lowest value to min_stack
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        # If min_stack is empty, nothing to compare, append val
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from stack as normal and from min_stack to have current lowest value
        # at the top
        self.stack.pop()
        self.min_stack.pop()
            

    def top(self) -> int:
        # Return the top value of stack as normal
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top value of min_stack which is the current lowest value
        return self.min_stack[-1]
        

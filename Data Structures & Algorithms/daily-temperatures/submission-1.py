class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with all 0s
        res = [0] * len(temperatures)
        # Stack will hold values we iterate through so that we only have to iterate
        # through the array once
        stack = [] # [temperature, index] pair

        for i, t in enumerate(temperatures):
            # For this current temperature, if there are values in the stack
            # and the top stack value is less than this current temperature,
            # then this current temperature is the closest higher temperature
            # for that top stack value. (Can iterate multiple times or none)
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = (i - stack_index)
            
            stack.append([t, i])

        # No need to go back and set all remaining values to zero
        # since we initialized res to be all 0s
        return res


                
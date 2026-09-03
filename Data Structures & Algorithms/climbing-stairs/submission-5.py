class Solution:
    def climbStairs(self, n: int) -> int:
        # Write a helper function that if the current steps is 2 or higher, then recursively
        # call the helper function to run on those split steps
        # If a new number of remaining steps is new, save number of unique ways to take it
        # into hashmap solved, so that we don't have to do expensive recalculations
        solved = {}

        def countWays(n):
            # If only one step left, only 1 distinct way to climb
            if n == 1:
                return 1
            # If only 2 steps, only 2 unique ways to climb
            elif n == 2:
                return 2
            # If more than 2 steps, do recursive call to get the unique remaining ways you can go through
            # the rest of the staircase if you take 2 steps and if you took 1 step 
            elif n > 2:
                # If already calculated, retrieve value from hashmap
                if n in solved:
                    return solved[n]
                # If new, calculate unique ways, save to hashmap and return value
                else:
                    new_entry = countWays(n-2) + countWays(n-1)
                    solved[n] = new_entry
                    return new_entry
            # Top reached, no steps can be taken
            else:
                return 0
        
        return countWays(n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort the position list in descending order so that we begin 
        # by processing the car closest to the destination
        # We do this so that when future cars are processed, we can determine 
        # whether they are becoming a fleet with the car in front of them
        hmap = {}
        for i in range(len(position)):
            hmap[position[i]] = speed[i]

        position.sort(reverse=True)

        stack = []

        # Iterate through each car, and if a car would reach the target before the 
        # car in front of it, they become a part of the same car fleet
        for i in range(len(position)):
            time = (target - position[i]) / hmap[position[i]]
            
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
                
        return len(stack)
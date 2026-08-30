class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ### Brute Force approach
        # # Start at speed 1 and increment speed by 1 until we can finish the bananas in time

        # # Boolean max reached is our while loop conditional and will only be switched to True when
        # # we can finally finish all bananas, thus ending the while loop
        # max_reached = False
        # speed = 1

        # while not max_reached:
        #     # Running counter for hours needed to eat with the current speed
        #     cur_hours = 0

        #     # Calculate total hours needed to eat with current speed
        #     for i in piles:
        #         cur_hours += math.ceil(i / speed)

        #     # If we eat the bananas too slow, increase our eating speed and continue looping
        #     if cur_hours > h:
        #         speed += 1
        #     else:
        #         max_reached = True
                

        # return speed

        ### Actual

        # Optimal eating speed is between 1 and the max pile in piles
        l = 1
        r = max(piles)

        # best_speed will hold lowest valid speed
        best_speed = max(piles)

        # Use binary search to find optimal eating speed
        while l <= r:
            # Get middle speed between l and r
            middle = (l + r) // 2

            # Calculate the amount of hours, cur_hours, it would take to eat all banana piles with current speed
            cur_hours = 0
            for i in piles:
                cur_hours += math.ceil(i / middle)
            
            # If cur_hours is within h bound, then check if better than best, and reduce right boundary
            # to below the middle speed
            if cur_hours <= h:
                if middle < best_speed:
                    best_speed = middle

                r = middle - 1
            # Middle speed is too slow, move l to right of middle speed
            else:
                l = middle + 1
        
        return best_speed
                

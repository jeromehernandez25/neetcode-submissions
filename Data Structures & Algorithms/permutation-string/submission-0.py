class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s2 can never contain s1
        if len(s1) > len(s2):
            return False
        
        # Create a count for the unique characters in string 1
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        need = len(count1)
        for i in range(len(s2)):
            # Initialize a dictionary count2 to keep track of characters in current window
            # If a character count in count2 is greater than count1, window cannot contain s1, break
            # If a character count in count2 matches count1, amount of unique characters needed is same, incremenet cur
            # if cur matches the amount of unqiue character count matches needed, return True
            count2 = {}
            cur = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1

                # check if count2 is above count1
                if count2.get(s2[j], 0) > count1.get(s2[j], 0):
                    break
                # check if count 2 is equal to count1
                if count2.get(s2[j], 0) == count1.get(s2[j], 0):
                    cur += 1
                if cur == need:
                    return True
        
        return False
            

            


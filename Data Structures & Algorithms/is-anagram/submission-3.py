class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a dictionary to hold number of each letter in string s
        dictionary = {}
        for i in s:
            dictionary[i] = dictionary.get(i, 0) + 1 
        
        # Iterate through string t
        for i in t:
            # If letter not in string s or has count 0, mismatch
            if dictionary.get(i) is None or dictionary.get(i) == 0:
                return False
            # Letter exists in string s, minus from its running count
            else:
                dictionary[i] -= 1
        
        # Iterate through disctionary and check if all values are 0
        for i in dictionary.values():
            # If a value is not 0, mismatch return false
            if i != 0:
                return False

        # String t matches string s 
        return True
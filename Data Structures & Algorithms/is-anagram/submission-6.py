class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if strings are of same length
        if len(s) != len(t):
            return False
        
        # Create a dictionary to hold number of each letter in string s
        dictionary = {}
        for i in s:
            dictionary[i] = dictionary.get(i, 0) + 1 
        
        # Iterate through string t
        for j in t:
            # If character not in dictionary, string t is not an anagram of string s
            if j not in dictionary:
                return False
            # If letter exists in string s, minus from its running count
            else:
                dictionary[j] -= 1
                if dictionary[j] < 0:
                    return False

        # String t matches string s 
        return True
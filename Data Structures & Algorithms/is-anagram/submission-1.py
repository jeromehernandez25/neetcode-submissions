class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in s:
            dictionary[i] = dictionary.get(i, 0) + 1 
        
        for i in t:
            if dictionary.get(i) is None or dictionary.get(i) == 0:
                return False
            else:
                dictionary[i] -= 1
        
        if all(i == 0 for i in dictionary.values()):
            return True

        return False
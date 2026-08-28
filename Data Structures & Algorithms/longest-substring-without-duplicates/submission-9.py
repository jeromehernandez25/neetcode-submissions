class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Move the left pointer through each character in string
        # Put character at left pointer into temporary dictionary
        # Iterate, incrementing right pointer and checking that the character
        # doesn't already exist in the dictionary, add 1 to running count,
        # If it already exists in dictionary, compare running count vs longest substring
        # break loop to increment left pointer, and increment right pointer and continue comparing
        # End loop if right pointer reaches end of array or left reach end of array

        # if not s: # If string is empty, return 0
        #     return 0

        # dictionary = {}
        # n = len(s)

        # best = 0

        # for i in range(n-1): # Iterate through each character in string s
        #     dictionary[s[i]] = i # save character's value as its index in dictionary

        #     for j in range(i+1, n): 
        #         if s[j] in dictionary:
        #             # get number of entries currently in dictionary
        #             cur_len = len(dictionary)
        #             # compare to current best substring length
        #             if cur_len > best:
        #                 best = cur_len

        #             # set left index to be after char's old index
        #             i = dictionary[s[j]] + 1
        #             # remove all dictionary pairs with values less than char's old index
        #             for key in list(dictionary.keys()):
        #                 if dictionary[key] < i:
        #                     del dictionary[key]

        #             # set dictionary value of cur char to new index
        #             dictionary[s[j]] = j
        #             break
                
        #         dictionary[s[j]] = j
                

        # return best

        mp = {}     # Map will store the last index of each character
        l = 0       # left pointer
        best = 0    # variable to hold best substring length

        for r in range(len(s)): # Move right pointer throuhg entire character arrary
            if s[r] in mp:      # If char is in map already
                l = max(mp[s[r]] + 1, l) # Then move left pointer past char's previous index, but never backwards
            mp[s[r]] = r                    # Update index of char at right index
            best = max(best, r - l + 1)     # Update best substring length

        return best
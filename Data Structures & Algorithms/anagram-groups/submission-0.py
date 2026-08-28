class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Variables to save lists of dictionaries and list of grouped strings
        dict_list = []
        str_list = []

        # Iterate through each string in string array
        for string in strs:

            # Get dictionary for current string
            cur_dictionary = {}
            for s in string: 
                cur_dictionary[s] = cur_dictionary.get(s, 0) + 1
            
            # Iterate through current dict_list 
            match_found = False
            for index, l in enumerate(dict_list): # Find matching dictionary
                if cur_dictionary == l:
                    match_found = True
                    str_list[index].append(string)
                    break
            
            # If no match found, add cur_dictionary to dict_list and string to its own sublist
            if not match_found:
                dict_list.append(cur_dictionary)
                str_list.append([string])
            
        return str_list
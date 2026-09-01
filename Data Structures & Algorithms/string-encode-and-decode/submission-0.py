class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        # For each string in the string array
        # append the length of the string, with delimiter #, along with the string itself to encoded_string
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        # Initialize string array to hold decoded strings
        decoded_string = []
        i = 0
        
        # Decode strings until the i pointer reaches the end
        while i < len(s):
            j = i

            # Use j to record where delimiter # is
            while s[j] != "#":
                j += 1
            
            # Use i and j to get amount of characters in this string
            length = int(s[i:j])
            
            # Set i to start of this string and j to the end of this string
            i = j + 1
            j = i + length
            
            # Append the string to the decoded string array
            decoded_string.append(s[i:j])

            # Move pointer to the start of next string's prefix
            i = j

        return decoded_string

            


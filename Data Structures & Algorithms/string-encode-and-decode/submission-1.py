class Solution:
    # Encode string by appneding the length of the string and the delimiter #
    # to each string
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            length = str(len(s))
            encoded_string += length + "#" + s
        
        return encoded_string

    # Decode string by first reading the leading integer of how many strings to read
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        index = 0
        while index < len(s) - 1:

            # Read the prefix length of the string to find out how many chars
            # to read for this current string
            chars_to_read = 0
            while s[index] != "#":
                chars_to_read = chars_to_read * 10 + int(s[index])
                index += 1
            
            # Move index past delimiter and get current string
            index += 1
            current_string = ""
            while chars_to_read:
                current_string += s[index]
                index += 1
                chars_to_read -= 1
            
            # Append current string to decoded string
            decoded_string.append(current_string)
        
        return decoded_string

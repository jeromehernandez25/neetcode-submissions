class Solution:
    def isPalindrome(self, s: str) -> bool:
        # eliminate all whitespace and convert letters to lowercase
        punctuated_string = s.replace(" ", "").lower()
        # eliminate punctuation
        string = re.sub(r'[^\w\s]', '', punctuated_string)
        n = len(string)


        # iterate from both start and end of string meeting in middle
        for i in range(n // 2):
            # compare front and back indexes
            front_char = string[i]
            back_char = string[n-i-1]
            if front_char != back_char:
                return False

        return True
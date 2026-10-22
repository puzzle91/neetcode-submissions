class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for letter in s.lower():
            if letter.isalnum():
               clean_s += letter
        
        return True if clean_s == clean_s[::-1] else False
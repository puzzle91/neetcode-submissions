class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = "".join([x.lower() for x in s if x.isalnum()])

        if s_ == s_[::-1]:
            return True
        return False
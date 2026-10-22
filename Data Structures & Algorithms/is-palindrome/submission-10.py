class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = "".join([x.lower() for x in s if x.isalnum()])

        left, right = 0, len(s_) - 1

        while left <= right:

            if s_[left] != s_[right]:
                return False
            left += 1

            right -= 1

        return True
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = defaultdict(int)
        max_length = 0


        for r in range(len(s)):
            c = s[r]
            seen[c] +=1 

            while seen[c] > 1:
                left_c = s[l]
                seen[left_c] -=1
                l+=1

            if seen[c] == 0:
                del seen[c]
            max_length = max(max_length, r - l + 1)
        return max_length
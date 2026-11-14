from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            c = s[right]
            seen[c] += 1

            # Remove characters from the left until the duplicate is gone.
            while seen[c] > 1:
                seen[s[l]] -= 1
                l += 1

            max_length = max(max_length, right - l + 1)

        return max_length
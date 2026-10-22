class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0  # Highest frequency of a single char in window
        count = {}
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # Print the window for visualization
            window = s[left : right + 1]
            print(
                f"Window: [{left}:{right}] '{window}' | counts: {dict(count)} | max_count: {max_count}"
            )

            # (window size) - (most frequent char count) = chars to replace
            if (right - left + 1) - max_count > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1

            result = max(result, right - left + 1)

        print("Final result:", result)
        return result
        
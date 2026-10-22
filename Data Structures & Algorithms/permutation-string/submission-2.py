

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        remaining = Counter(s1)

        def backtrack(j: int, needed: int) -> bool:
            if needed == 0:
                return True
            if j == len(s2) or remaining[s2[j]] == 0:
                return False

            char = s2[j]
            remaining[char] -= 1
            found = backtrack(j + 1, needed - 1)
            remaining[char] += 1
            return found

        return any(
            backtrack(start, len(s1))
            for start in range(len(s2) - len(s1) + 1)
        )
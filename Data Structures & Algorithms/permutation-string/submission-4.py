class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         
        if len(s1) > len(s2):
            return False

        target = defaultdict(int)
        for c in s1:
            target[c] +=1

        l = 0
        seen  = defaultdict(int)

        for right in range(len(s2)):
            c = s2[right]
            seen[c] += 1

            # Keep the window at most as long as s1.
            if right - l + 1 > len(s1):
                left_char = s2[l]
                seen[left_char] -= 1

                # Remove zero counts so dictionary equality works.
                if seen[left_char] == 0:
                    del seen[left_char]

                l += 1

            if seen == target:
                return True

        return False

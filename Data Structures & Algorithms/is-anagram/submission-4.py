class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS: dict[int] = {}
        countT: dict[int] = {}

        if len(s) != len(t):
            return False
        else:
            for idx in range(len(s)):

                if s[idx] in countS:
                    countS[s[idx]] = countS.get(s[idx], 0) + 1
                else:
                    countS[s[idx]] = 1

                if t[idx] in countT:
                    countT[t[idx]] = countT.get(t[idx], 0) + 1
                else:
                    countT[t[idx]] = 1


        return countT == countS
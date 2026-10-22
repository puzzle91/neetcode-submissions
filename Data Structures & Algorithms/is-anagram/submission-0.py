class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        repeated = {}
        for i in s:
            if i not in t:
                return False
            else:
                repeated[i] = repeated.get(i, 0) + 1

        for v,i in repeated.items():
            if s.count(v) != t.count(v):
                return False
                
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_ = [x for x in s]
        t_ = [z for z in t]
        s_.sort()
        t_.sort()
       

        for v1, v2 in zip(s_, t_):
            if v1 != v2:
                return False
        return True 
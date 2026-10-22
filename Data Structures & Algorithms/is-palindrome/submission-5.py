class Solution:
    def isPalindrome(self, s: str) -> bool:
      
         

        s = "".join([x.lower() for x in s if x.isalnum()])
        print(s, "here")
        if len(s) == 0:
            return True
        if s[0] != s[-1]:
            return False

        for v in range(1, len(s)):
            prefix = s[v]
            suffix = s[len(s) - v - 1]
            
            if prefix != suffix:    
                return False
        
        return True  
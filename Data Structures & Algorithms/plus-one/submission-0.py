class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = int("".join([str(x) for x in digits])) + 1
     
        tmp = [int(x) for x in str(res)]
        return tmp
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        possible_letters = []

        for d in digits:
            possible_letters.append([x for x in keypad[d]])
        print(possible_letters)

        seen = {}
        def backtrack(i, path):
           
           
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return

            
            for c in keypad[digits[i]]:
                path.append(c)
                backtrack(i+1, path)
                path.pop()

                    
                        
        if digits:
        
            backtrack(0, [])
        return res



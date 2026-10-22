class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return False
        for n in nums:
            if nums.count(n) >= 2:
                print(f"Found duplicate {n}")
                s = True
                break
            s = False
        print(f"Returning ====> {s}")
        return s
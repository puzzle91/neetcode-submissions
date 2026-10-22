class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        if len(nums) > len(set(nums)):
            return True
        return False


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        size = len(nums)
        write = 2  # first two elements are always allowed

        for read in range(2, size):
            # keep current number only if it does not create 3 duplicates in a row
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write

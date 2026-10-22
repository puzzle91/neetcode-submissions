class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map: dict[str, int] = {}
        for n, num in enumerate(nums):

            complement = target - num
            if num not in num_map:
                num_map[num] = n
            if complement in num_map:
                if n != num_map[complement]:
                    return [num_map[complement], n]
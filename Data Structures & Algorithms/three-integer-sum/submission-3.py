class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0 
        ans = []
        for i in range(len(nums)):
            # Optional: skip duplicates for uniqueness
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    # record triplet
                    triplet = [nums[i], nums[left], nums[right]]
                
                    if triplet not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return ans

        

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        print(*height, sep="\n")
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    # Water can be trapped here
                    water_trapped += left_max - height[left]
                    print(f"{water_trapped = }")
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                    print(f"{right_max = }")
                else:
                    # Water can be trapped here
                    water_trapped += right_max - height[right]
                    print(f"{water_trapped =  }")
                right -= 1

        return water_trapped

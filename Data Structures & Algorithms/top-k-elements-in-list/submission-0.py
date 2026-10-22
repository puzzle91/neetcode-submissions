class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_map = {}

        for n, num in enumerate(nums):
            if num not in seen_map:
                seen_map[num] = 1
            else:
                seen_map[num] = seen_map.get(num, 0) + 1

        seen_map = sorted(seen_map.items(), key=lambda x: x[1], reverse=True)
        print("seen map", seen_map)

        res = [seen_map[x][0] for x in range(k)]
        print("result", res)
        return res
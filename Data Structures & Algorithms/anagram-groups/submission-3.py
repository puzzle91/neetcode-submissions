class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s1 = strs.copy()
        size_maps: list[tuple[str, ...]] = [tuple(sorted(x)) for x in s1]
        size_hash: dict[tuple[str, ...], list[str]] = {}
        for i in range(len(size_maps)):
            curr_map = size_maps[i]

            if curr_map not in size_hash:
                size_hash[curr_map] = [s1[i]]

            else:
                size_hash[curr_map] = size_hash.get(curr_map, []) + [s1[i]]

        print([x for x in size_hash.values()], "size_hash")
        return sorted(list(size_hash.values()), key=lambda x: len(x))
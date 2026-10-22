class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def helper_func(input_str: str):
            seen_chars: dict[str, int] = {}

            for i in range(len(input_str)):
                if input_str[i] not in seen_chars:
                    seen_chars[input_str[i]] = 1
                else:
                    seen_chars[input_str[i]] = seen_chars.get(input_str[i], 0) + 1
            return seen_chars
        s1 = strs
        seen_maps = []
        size_map = []
        seen_idx: set[int] = set()
        for i in range(len(s1)):
            mapper = helper_func(s1[i])

            if i not in seen_idx and s1[i] not in size_map:
                size_map += [s1[i]]
                seen_idx.add(i)
                for j in range(i + 1, len(s1)):
                    mapper_2 = helper_func(s1[j])
                    if mapper_2 == mapper and j not in seen_idx:
                        seen_idx.add(j)
                        size_map += [s1[j]]

            (
                seen_maps.append(size_map)
                if len(size_map) > 0 and size_map not in seen_maps
                else None
            )
            size_map = []
        print("SEEN MAPs", seen_maps)
        return seen_maps
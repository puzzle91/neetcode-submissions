class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for wrd in strs:
            key = tuple(sorted(wrd))
            if key in cache:
                cache[key] = cache.get(key, []) + [wrd]
            else:
                cache[key] = [wrd]
        

        cache = sorted(cache.values(), key=lambda x: len(x))
        return cache 
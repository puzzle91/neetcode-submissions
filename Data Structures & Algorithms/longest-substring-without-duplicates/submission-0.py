class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        arr = [x for x in s]
        mx_size = 0
        for right in range(len(arr)):
            wdw = arr[left: right + 1 ]
            if len(wdw) == len(set(wdw)):
                mx_size = max(len(wdw), mx_size)
            else:
                left+=1
        return mx_size
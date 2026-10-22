class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        arr = [x for x in s]
        mx_size = 0
        sub =  set()
        for right in range(len(arr)):
            while arr[right] in sub:
                sub.remove(arr[left])

                left+=1
            sub.add(arr[right])
            if len(sub) >= mx_size:
                mx_size = len(sub)
        return mx_size
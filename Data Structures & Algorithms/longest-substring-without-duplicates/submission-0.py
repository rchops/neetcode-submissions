class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window with set
        l, r = 0, 0
        seen = set()
        long = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                long = max(long, r-l)
            else:
                seen.remove(s[l])
                l += 1
        
        return long
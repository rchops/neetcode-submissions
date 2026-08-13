class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use sliding window
        # k is paramter to stay under
        # want to check if length of sliding window - most freq char > k
        # use hash table to keep track of most freq char
        chars = defaultdict(int)
        l = 0
        count = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            while (r - l + 1) - max(chars.values()) > k:
                # remove left chars till valid again
                chars[s[l]] -= 1
                l += 1
            
            count = max(count, r-l+1)

        return count
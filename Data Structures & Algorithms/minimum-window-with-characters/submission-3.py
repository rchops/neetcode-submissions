class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use dynamic sliding window with hashmap
        # always add element to sliding window then check condition
        # remove while string still matches to get shortest
        window, t_hash = {}, {}

        for c in t:
            t_hash[c] = 1 + t_hash.get(c, 0)

        res, lenres = [-1, -1], float("inf")
        l = 0
        have, need = 0, len(t_hash)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_hash and window[c] == t_hash[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < lenres:
                    lenres = (r - l + 1)
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in t_hash and window[s[l]] < t_hash[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return "".join(s[l:r+1]) if lenres != float("inf") else "" 
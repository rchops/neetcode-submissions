class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use fixed sliding window of size len(s1)
        # use hash map to keep count of num of letters
        if len(s1) > len(s2):
            return False

        s1_hash = defaultdict(int)
        for s in s1:
            s1_hash[s] += 1

        curr = defaultdict(int)
        for i in range(len(s1)):
            curr[s2[i]] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if curr == s1_hash:
                return True
            curr[s2[r]] += 1
            curr[s2[l]] -= 1
            if curr[s2[l]] == 0:
                curr.pop(s2[l])
            l += 1

        return curr == s1_hash
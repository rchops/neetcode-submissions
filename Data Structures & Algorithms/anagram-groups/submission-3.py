class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hash table for results
        # use freq of each letter as key
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())
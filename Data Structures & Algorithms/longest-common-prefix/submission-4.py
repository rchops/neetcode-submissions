class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # compare all strings at same letter
        # range of len of first string
        # go through strs and check:
            # is pointer > len of string -> return
            # if letter is same
        res = []
        for i in range(len(strs[0])):
            for word in strs:
                if i > (len(word)-1) or word[i] != strs[0][i]:
                    return "".join(res)
            res.append(strs[0][i])

        return "".join(res)
            
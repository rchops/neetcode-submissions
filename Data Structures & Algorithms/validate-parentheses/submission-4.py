class Solution:
    def isValid(self, s: str) -> bool:
        # use hashmap with closing for keys for each pair
        # use stack for comparisons
        # if its close parenthesis check if val = top of stack
        # otherwise means its still opening and add to stack
        close_to_open = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True

        return False
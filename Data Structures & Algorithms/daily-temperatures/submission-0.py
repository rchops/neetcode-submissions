class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic stack with index and temp to keep track
        # if greater than last element on stack calculate diff, add to res, pop
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackInd = stack[-1][1]
                res[stackInd] = (i - stack[-1][1])
                stack.pop()
            stack.append([t, i])

        return res
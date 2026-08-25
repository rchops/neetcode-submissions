class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use monotonically increasing stack
        # store idx + height pair
        # push idx back as far as can go
        # update max area
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                # check before removing if max area of one being removed greater
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        # go through whats left in stack and see if any are max
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
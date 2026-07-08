class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # try using dynamic sliding window
        # start at beginning - check if next one is valid
        # if not compare next and decide max
        # if valid add and move till not valid, then go back and add too
        # pointer to keep track of left of sliding window, right of sliding window
        current = 0
        sliding = 0
        biggest = 0
        while current in range(len(heights)):
            sliding = 0
            # set current height to current height we are comparing everything
            # to in array -> one the right pointer is at
            current_height = heights[current]
            # while in range and next one is greater or equal keep adding curr_height
            # until not valid right
            forward = current
            sliding += current_height
            while (forward+1) < len(heights) and current_height <= heights[forward+1]:
                sliding += current_height
                forward += 1
            # once not valid, start adding left till not valid
            backward = current
            while backward > 0 and current_height <= heights[backward-1]:
                sliding += current_height
                backward -= 1
            
            biggest = max(biggest, sliding)
            current += 1
        
        return biggest
            
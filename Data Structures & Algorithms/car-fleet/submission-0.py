class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # use stack to figure out if cars catch up
        # use time it takes to get to target
        # join arrays and sort - start from distance closest to end
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
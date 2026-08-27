class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound is max out of all piles
        # use binary search between 1 and max to find which val is best
        # sort array and get max
        piles.sort()
        largest = piles[-1]
        l, r = 1, largest
        k = largest

        # if time <= h - set r = mid - 1 and store best
        # if time > h - set l = mid + 1
        # get time using ciel(x/k) for each pile
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            if time <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1

        return k
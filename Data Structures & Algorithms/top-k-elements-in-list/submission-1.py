from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use max heap with key as freq
        # invert for max heap
        heap: list[tuple[int, int]] = []
        nums.sort()
        l, r = 0, 0
        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            heappush(heap, (-(r-l), nums[l]))
            l = r

        res = []
        for i in range(len(heap)):
            print(heap[i])

        for _ in range(k):
            _, r = heappop(heap)
            res.append(r)

        return res
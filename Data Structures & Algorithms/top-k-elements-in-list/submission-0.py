from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort array
        # use sliding window/two pointers to count num of each int
        # use pq
        arr_sorted = sorted(nums)
        l, r = 0, 0
        res = []
        heap: list[tuple[int, int]] = []
        while r < len(nums):
            while r < len(nums) and arr_sorted[l] == arr_sorted[r]:
                r += 1
            
            heappush(heap, (-(r-l), arr_sorted[l]))
            l = r
        
        for i in range(len(heap)):
            print(heap[i])

        for _ in range(k):
            _, r = heappop(heap)
            res.append(r)
        
        return res

        

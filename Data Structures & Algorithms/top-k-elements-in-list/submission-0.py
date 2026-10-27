class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for n in nums:
            freq_map[n] = 1 + freq_map.get(n, 0)

        # we use a min heap based on frequency and choose the k most frequent at the end

        min_h = []

        for num, freq in freq_map.items():
            heapq.heappush(min_h, (freq, num))

            if len(min_h) > k:
                heapq.heappop(min_h)

        freq_elm = []
        for i in range(k):
            freq_elm.append(heapq.heappop(min_h)[1])

        return freq_elm
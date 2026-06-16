class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counts of elements
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        # sort elements into buckets by their count
        buckets = defaultdict(list)
        for n, count in counts.items():
            buckets[count].append(n)

        res = []
        # loop from len(nums) to 1 adding elements, break when len(res) == k
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

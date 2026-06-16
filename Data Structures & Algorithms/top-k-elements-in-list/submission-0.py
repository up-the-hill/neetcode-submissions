class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = defaultdict(list)
        res = []
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        for num, count in counts.items():
            buckets[count].append(num)
        res = []
        for i in range(len(nums)):
            for num in buckets[len(nums) - i]:
                res.append(num)
            if len(res) == k:
                return res

        return res





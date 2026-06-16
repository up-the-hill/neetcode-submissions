class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counts of all the elements in a dict.
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        # reverse the dict
        buckets = defaultdict(list)
        for number, count in d.items():
            buckets[count].append(number)

        # loop from len(nums) to 0, return when K elements have been added
        res = []
        for i in range(len(nums), 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res

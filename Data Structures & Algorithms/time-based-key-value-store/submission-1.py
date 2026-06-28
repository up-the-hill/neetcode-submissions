class TimeMap:

    def __init__(self):
        self.hmap = {} # maps keys to a list of (timestamp, value) pairs


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        res = ""
        li = self.hmap[key]
        l, r = 0, len(li) - 1
        while l <= r:
            m = (l + r) // 2
            mid = li[m]
            if mid[0] == timestamp:
                return mid[1]
            elif mid[0] < timestamp:
                res = mid[1]
                l = m + 1
            else:
                r = m - 1
        return res


        

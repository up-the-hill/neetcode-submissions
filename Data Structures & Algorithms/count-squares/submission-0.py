class CountSquares:

    def __init__(self):
        self.ptCount = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.ptCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.ptCount.keys()):
            found = 0
            if (
                px == x or
                py == y or
                abs(px - x) != abs(py - y)
            ):
                continue
            found += self.ptCount[(x, py)] * self.ptCount[(px, y)]
            found *= self.ptCount[(x, y)]
            res += found
        
        return res



        

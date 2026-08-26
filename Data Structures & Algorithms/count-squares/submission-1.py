class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        i, j = point
        res = 0
        for x, y in list(self.points.keys()):
            if abs(x-i) == abs(y-j) and x != i and y != j: # on same diagonal
                res += self.points[(x,y)] * self.points[(x,j)] * self.points[(i,y)]

        return res


        

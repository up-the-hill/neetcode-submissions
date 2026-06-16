class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        for c in cars:
            t = (target - c[0]) / c[1] # d / s
            if s and s[-1][1] >= t: # if the car ahead takes longer than this car, a car fleet is formed, ignore this car
                continue
            s.append((c, t))

        return len(s)

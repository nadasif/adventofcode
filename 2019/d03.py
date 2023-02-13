import os

class Point:
    _cache = dict()
    def __new__(cls, x, y):
        key = f'{x}:{y}'
        if key not in cls._cache:
            cls._cache[key] = object.__new__(cls)
        return cls._cache[key]

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self):
        self._points = set()
        self._x = 0
        self._y = 0

    def go(self, path):
        for step in path.split(","):
            self.step(step)

    def step(self, step):
        if step[0] in ['L', 'R']:
            pass
        else:
            pass

def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def main():
    text = loadData()


    print(id(Point(1,1)))
    print(id(Point(1,2)))
    print(id(Point(1,2)))
    print(id(Point(1,1)))

    print("\nPart 1")

    print("\nPart 2")


if __name__ == "__main__":
    main()

import os.path

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


def log(text):
    print(text)
    pass

def loadData():
    filename = f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt"
    file1 = open(filename, 'r')
    text = file1.read()
    file1.close()
    return text

def main():
    text = loadData()
    log(text)

    print(id(Point(1,1)))
    print(id(Point(1,2)))
    print(id(Point(1,2)))
    print(id(Point(1,1)))



if __name__ == '__main__':
    main()

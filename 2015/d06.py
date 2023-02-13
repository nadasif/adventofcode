import os

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(1000)] for _ in range(1000)]

    def do(self, cmd):
        p = cmd.split()
        op, c1, _, c2 = p[-4:]
        x1, y1, x2, y2 = map(int, f'{c1},{c2}'.split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2+1):
                if op == "toggle":
                    self.grid[x][y] = 1 if self.grid[x][y] == 0 else 0
                else:
                    self.grid[x][y] = 1 if op == "on" else 0

    def do2(self, cmd):
        p = cmd.split()
        op, c1, _, c2 = p[-4:]
        x1, y1, x2, y2 = map(int, f'{c1},{c2}'.split(','))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2+1):
                if op == "toggle":
                    self.grid[x][y] += 2
                else:
                    self.grid[x][y] = max(0, self.grid[x][y] + (1 if op == "on" else -1))


def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def main():
    txt = loadData()

    print("\nPart 1")
    g = Grid()
    for line in txt.split('\n'):
        g.do(line)

    print(sum(c for row in g.grid for c in row))

    print("\nPart 2")
    g = Grid()
    for line in txt.split('\n'):
        g.do2(line)
    print(sum(c for row in g.grid for c in row))


if __name__ == "__main__":
    main()

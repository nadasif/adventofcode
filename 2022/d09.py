import os

class Command:
    _dxdy = {'L': (-1,0), 'R': (1,0), 'U': (0,1), 'D': (0,-1)}
    def __init__(self, txt):
        self.op, step = txt.split()
        self.dx, self.dy = Command._dxdy[self.op]
        self.steps = int(step)

    def __repr__(self):
        return f"#<Command: {self.op} {self.steps}>"

class Coord:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def touching(self, other):
        return abs(self.x - other.x)<=1 and abs(self.y - other.y)<=1

    def move(self, cmd: Command):
        return Coord(self.x + cmd.dx, self.y + cmd.dy)

    def follow(self, coord):
        if self.touching(coord): return self
        hx, hy = coord.x, coord.y
        tx, ty = self.x, self.y
        dx = 0 if hx == tx else (hx - tx) / abs(hx - tx)
        dy = 0 if hy == ty else (hy - ty) / abs(hy - ty)
        return Coord(tx + dx, ty + dy)

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y==other.y

class Plane:
    def __init__(self, n):
        self.knots = [Coord(0,0) for _ in range(n)]
        self.visited = set()
        self.visited.add(self.knots[n-1])

    def move(self, cmd: Command):
        n = len(self.knots)
        for _ in range(cmd.steps):
            self.knots[0] = self.knots[0].move(cmd)
            for i in range(1, n):
                self.knots[i] = self.knots[i].follow(self.knots[i-1])
            self.visited.add(self.knots[n-1])

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def main():
    txt = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
    txt = loadData('.in')
    cmds = list(map(Command, txt.split('\n')))
    # print(cmds)

    print("\nPart 1")
    plane = Plane(2)

    for cmd in cmds:
        plane.move(cmd)

    print(len(plane.visited))


    print("\nPart 2")
    plane = Plane(10)

    for cmd in cmds:
        plane.move(cmd)

    print(len(plane.visited))


    pass


if __name__ == "__main__":
    main()

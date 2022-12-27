import os

class Command:
    _dir = {'L': (-1,0), 'R': (1,0), 'U': (0,1), 'D': (0,-1)}
    def __init__(self, txt):
        parts = txt.split()
        self.dx, self.dy = Command._dir[parts[0]]
        self.code = parts[0]
        self.steps = int(parts[1])

    def __repr__(self):
        return f"#<Command: {self.code} {self.steps}>"

class Coord:
    def __init__(self,x,y):
        self.x, self.y = x, y

    def move(self, x, y):
        self.x += x
        self.y += y

    def isTouching(self, coord):
        return abs(self.x - coord.x)<=1 and abs(self.y - coord.y)<=1

    def xy(self):
        return self.x,self.y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

class Plane:
    def __init__(self):
        self.head = Coord(0,0)
        self.tail = Coord(0,0)
        self.visited = set()
        self.visited.add(self.tail)


    def move(self, cmd: Command):
        for _ in range(cmd.steps):
            self.head.move(cmd.dx, cmd.dy)
            if not self.tail.isTouching(self.head):
                hx, hy = self.head.xy()
                tx, ty = self.tail.xy()
                dx = 0 if hx == tx else (hx-tx) / abs(hx-tx)
                dy = 0 if hy == ty else (hy-ty) / abs(hy-ty)
                self.tail = Coord(tx+dx, ty+dy)
                self.visited.add(self.tail)

    def moveOld(self, cmd: Command):
        for i in range(cmd.steps):
            lastHead = Coord(self.head.x, self.head.y)
            self.head.move(*cmd.direction)
            if not self.head.isTouching(self.tail):
                self.tail = lastHead
                self.coords.append(self.tail)
        self.draw()

    def draw(self):
        minCd = Coord(self.head.x, self.head.y)
        maxCd = Coord(self.head.x, self.head.y)
        for crd in self.coords:
            minCd.x = min(minCd.x, crd.x)
            minCd.y = min(minCd.y, crd.y)
            maxCd.x = max(maxCd.x, crd.x)
            maxCd.y = max(maxCd.y, crd.y)

        grid = '.' * (maxCd.x - minCd.x + 1)
        grid = f'{grid}\n' * (maxCd.y - minCd.y + 1)
        dots = [[c for c in s] for s in grid.split('\n')]

        # dots = [['.'] * (maxCd.x - minCd.x + 1)] * (maxCd.y - minCd.y + 1)
        offx = minCd.x
        offy = minCd.y
        for crd in self.visited:
            dots[crd.y - offy][crd.x - offx] = 'T'

        dots[self.tail.y - offy][self.tail.x-offx] = 'L'
        dots[self.head.y - offy][self.head.x-offx] = 'H'

        grid = ''
        for a in dots:
            grid = f"{''.join(c for c in a)}\n{grid}"
        print(grid)

    def __repr__(self):
        return f"#<Plane: {self.head}, {self.tail}>"

class Part2:
    def __init__(self, txt):
        pass

    def __repr__(self):
        return f"#<P2:>"

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
    plane = Plane()

    # for i in range(71):
    #     print(f"{i}:{cmds[i]}")
    #     plane.move(cmds[i])
    #
    for cmd in cmds:
        plane.move(cmd)

    # print(plane)
    # print(plane.coords)
    # print(len(plane.coords))
    print(plane.visited)
    print(len(plane.visited))


    print("\nPart 2")


    pass


if __name__ == "__main__":
    main()

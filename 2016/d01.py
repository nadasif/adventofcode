import os.path

class Command:
    def __init__(self, txt):
        self.to = txt[0]
        self.steps = int(txt[1:])
    def __repr__(self):
        return f'{self.to}{self.steps}'

class Loc:
    def __init__(self, x=0, y=0):
        self.x, self.y = x,y
    def __repr__(self):
        return f'({self.x},{self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Grid:
    _move = {'N': (0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
    _to = {'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}, 'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'} }
    def __init__(self):
        self.loc, self.dir = Loc(), 'N'
        self.visitedTwice = None
        self.visited = {self.loc}

    def move(self, cmd: Command):
        self.dir = Grid._to[cmd.to][self.dir]
        x,y = Grid._move[self.dir]
        for i in range(cmd.steps):
            self.loc = Loc(self.loc.x + x, self.loc.y + y)
            if self.visitedTwice is None:
                if self.loc in self.visited:
                    self.visitedTwice = self.loc
                else:
                    self.visited.add(self.loc)

    def __repr__(self):
        return f'{self.loc} to {self.dir}'

def loadData():
    filename = f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt"
    f = open(filename, "r")
    txt = f.read().strip()
    f.close()
    return txt

def main():
    txt = loadData()
    lines = txt.split(', ')
    cmds = list(map(Command, lines))

    grid = Grid()
    for cmd in cmds:
        grid.move(cmd)

    print("\nPart 1")
    print(grid)

    print("\nPart 2")
    #print(grid.visited)
    print(grid.visitedTwice)


if __name__ == "__main__":
    main()

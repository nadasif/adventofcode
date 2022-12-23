import os


class Cell:
    def __init__(self, c):
        self.n = int(c)
        self.v = False
        self.s = 0

    def __repr__(self):
        return f"{self.n}{'*' if self.v else ' '} "


class Part2:
    def __init__(self, txt):
        self.grid = [[Cell(c) for c in s] for s in txt.split()]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def visibleCount(self):
        s = 0
        for r in range(self.rows):
            for c in range(self.cols):
                s += 1 if self.grid[r][c].v else 0

        return s

    def markVisible(self):
        for r in range(self.rows):
            self.grid[r][0].v = True
            self.grid[r][self.cols-1].v = True
            # horizontal
            left = self.grid[r][0].n
            right = self.grid[r][self.cols-1].n
            for c in range(self.rows):
                if self.grid[r][c].n > left:
                    self.grid[r][c].v = True
                    left = self.grid[r][c].n
                if self.grid[r][self.cols-1-c].n > right:
                    self.grid[r][self.cols - 1 - c].v = True
                    right = self.grid[r][self.cols - 1 - c].n

        for c in range(self.cols):
            self.grid[0][c].v = True
            self.grid[self.rows-1][c].v = True
            # vertical
            top = self.grid[0][c].n
            bot = self.grid[self.rows-1][c].n
            for r in range(self.rows):
                if self.grid[r][c].n > top:
                    self.grid[r][c].v = True
                    top = self.grid[r][c].n
                if self.grid[self.rows-1-r][c].n > bot:
                    self.grid[self.rows - 1 - r][c].v = True
                    bot = self.grid[self.rows - 1 - r][c].n


    def __repr__(self):
        return '\n'.join( ''.join(f"{cell}" for cell in cells) for cells in self.grid )


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data


def main():
    txt = loadData('.in')

    print("\nPart 1")
    grid = Part2(txt)
    grid.markVisible()
    print(grid)
    print(grid.visibleCount())

    print("\nPart 2")

    pass


if __name__ == "__main__":
    main()

import os

class Grid:
    def __init__(self, txt):
        self.grid = [[int(c) for c in lst] for lst in txt.split()]

    def visibleCount(self):
        rows, cols = len(self.grid), len(self.grid[0])

        def visible(i, j, direction, h):
            while 0 < i < (rows-1) and 0 < j < (cols-1):
                i, j = (i + direction[0], j + direction[1])
                if self.grid[i][j] >= h:
                    return False
            return True

        count = (cols + rows - 2) * 2
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                height = self.grid[r][c]
                if (visible(r, c, (-1, 0), height)  or
                        visible(r, c, (1, 0), height) or
                        visible(r, c, (0, -1), height) or
                        visible(r, c, (0, 1), height)):
                    count += 1

        return count

    def scenicScore(self):
        rows, cols = len(self.grid), len(self.grid[0])

        def calcScore(i, j, direction, h):
            if h==0: return 1
            n = 0
            while 0 < i < (rows-1) and 0 < j < (cols-1):
                i, j = (i + direction[0], j + direction[1])
                n += 1
                if self.grid[i][j] >= h:
                    break
            return n


        maxScore = 1
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                height = self.grid[r][c]
                scT = calcScore(r, c, (-1, 0), height)
                scB = calcScore(r, c, (1, 0), height)
                scL = calcScore(r, c, (0, -1), height)
                scR = calcScore(r, c, (0, 1), height)
                score = (scT * scB * scL * scR)
                if score > maxScore:
                    maxScore = score
        return maxScore

    def __repr__(self):
        return f"#<P1:>"

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data


def main():
    txt = loadData('.in')

    print("\nPart 1")
    grid = Grid(txt)
    print(grid.visibleCount())

    print("\nPart 2")
    print(grid.scenicScore())

    pass


if __name__ == "__main__":
    main()

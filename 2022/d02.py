import os

class Part1:
    def __init__(self, txt):
        a, b = txt.split()
        self.a = 'ABC'.index(a)
        self.b = 'XYZ'.index(b)
        self.score = self.b + 1
        if self.b == self.a:
            self.score += 3
        if (self.a == self.b - 1) or (self.a == self.b + 2):
            self.score += 6

    def __repr__(self):
        rps = 'RPS'
        return f"{rps[self.a]}-{rps[self.b]} ({self.score})"

class Part2:
    def __init__(self, txt):
        a, b = txt.split()
        self.a = 'ABC'.index(a)
        self.score = 'XYZ'.index(b) * 3
        if b == 'X': # lose -> R-S, P-R, or S-P -> 0-2, 1-0, 2-1
            self.b = [2,0,1][self.a]
        elif b == 'Y': # draw -> R-R, S-S, P-P
            self.b = self.a
        else: # win -> R-P, P-S, S-R -> 0-1, 1-2, 2-0
            self.b = [1,2,0][self.a]
        self.score += self.b + 1

    def __repr__(self):
        rps = 'RPS'
        return f"{rps[self.a]}-{rps[self.b]} ({self.score})"


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def score(g):
    return g.score

def main():
    txt = loadData('.in')
    lines = txt.split('\n')

    print("\nPart 1")
    p1s = list(map(Part1, lines))
    #print(p1s)
    print( sum(map(score, p1s)))

    print("\nPart 2")
    p2s = list(map(Part2, lines))
    #print(p2s)
    print(sum(map(score, p2s)))


    pass


if __name__ == "__main__":
    main()

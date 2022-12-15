import os

class Part1:
    def __init__(self, txt):
        s1, s2 = map(lambda l: set(range(int(l[0]), int(l[1]) + 1)), map(lambda s: s.split('-'), txt.split(',')))
        self.score = 1 if s1.issubset(s2) or s2.issubset(s1) else 0
        pass

    def __repr__(self):
        return f"#<P1: {self.score}>"

class Part2:
    def __init__(self, txt):
        s1, s2 = map(lambda l: set(range(int(l[0]), int(l[1]) + 1)), map(lambda s: s.split('-'), txt.split(',')))
        self.score = 0 if len(s1 & s2) == 0 else 1

    def __repr__(self):
        return f"#<P1: {self.score}>"


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def score(p):
    return p.score

def main():
    txt = loadData('.in')
    lines = txt.split('\n')

    print("\nPart 1")
    p1s = list(map(Part1, lines))
    print(sum(map(score, p1s)))

    print("\nPart 2")
    p2s = list(map(Part2, lines))
    print(sum(map(score, p2s)))


    pass


if __name__ == "__main__":
    main()
